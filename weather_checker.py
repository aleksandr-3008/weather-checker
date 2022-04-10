import requests
import websockets
import asyncio


class WxChecker:
    """
    version 0.0.1

    This class creates connection to a client via local port an receives an information with wanted aerodromes.
    Then it sends a request to a certain API 'https://api.checkwx.com' and handles an information of weather
    on the given aerodromes. It sends back a message with the information about whether aerodromes are suitable
    or not
    """
    API_HEADER = {'X-API-Key': '783eba700d804544bab9e90f2c'}
    ARPT_MIN_WX = {'visibility': 800, 'ceiling': 80}

    def __init__(self):
        self.weather_report = {}

    async def main(self):
        async with websockets.serve(self._websocket_server, "localhost", 8765, ping_interval=None):
            await asyncio.Future()

    async def _websocket_server(self, websocket):

        list_of_airports = await websocket.recv()

        list_of_airports = list_of_airports.split(',')
        self.airport_set = set(list_of_airports)

        await websocket.send(str(self._wx_request()))

    def _wx_request(self):

        url = ''.join(('https://api.checkwx.com/metar/', ','.join(self.airport_set), '/decoded'))

        weather_in_airports = requests.get(url, headers=WxChecker.API_HEADER)

        for airport in weather_in_airports.json()['data']:

            icao_code = airport['icao']
            visibility = 0
            ceiling = 0

            if all(param in airport.keys() for param in ('visibility', 'ceiling')):
                visibility = airport['visibility']['meters_float']
                ceiling = airport['ceiling']['meters']
            elif 'CAVOK' in airport['raw_text']:
                visibility = 9999
                ceiling = 9999

            if ceiling < WxChecker.ARPT_MIN_WX['ceiling'] or visibility < WxChecker.ARPT_MIN_WX['visibility']:
                self.weather_report[icao_code] = f"Meteorological conditions are poor. This airport is not required " \
                                                 f"as destination or alternative. Visibility is {visibility}, " \
                                                 f"ceiling is {ceiling}"
            else:
                self.weather_report[icao_code] = f"Weather is good. Visibility is {visibility}, ceiling is {ceiling}"
            print(airport)
        return self.weather_report


if __name__ == '__main__':
    wx = WxChecker()
    asyncio.run(wx.main())
