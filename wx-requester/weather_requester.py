import asyncio
import datetime
import websockets
import os


class WxRequester:
    """
    version 0.0.1

    This class contains aerodromes that are wanted to be updated with current weather information. It also sends
    a ws request to a server which sends back a needed information and logs it into file.
    """

    def __init__(self):
        self.aerodromes_from_env = os.getenv('AERODROMES')
        self.set_of_aerodromes = {'ULLI', 'UUWW', 'USTR'}
        self.url = "ws://0.0.0.0:8765"

    async def requester(self):

        if self.aerodromes_from_env is None:  # check if user's variable was set
            pass
        else:
            self.aerodromes_from_env = str(self.aerodromes_from_env).strip().upper()
            self.set_of_aerodromes = set(self.aerodromes_from_env.split(','))

        while True:
            async with websockets.connect(self.url) as websocket:
                await websocket.send(','.join(self.set_of_aerodromes))

                weather = await websocket.recv()

                self.logger(weather)

                await asyncio.sleep(300)

    def logger(self, weather):

        time = datetime.datetime.now()

        with open('weather.log', mode='a', encoding='utf-8') as log:
            log.write('{0}  {1}\n'.format(time.strftime('%H:%M:%S %Y-%m-%d'), weather))


if __name__ == '__main__':
    wx = WxRequester()
    asyncio.run(wx.requester())
