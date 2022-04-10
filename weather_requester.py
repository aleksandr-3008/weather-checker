import asyncio
import datetime
import websockets


class WxRequester:
    """
    version 0.0.1

    This class contains aerodromes that are wanted to be updated with current weather information. It also sends
    a ws request to a server which sends back a needed information and logs it into file.
    """
    def __init__(self):
        self.set_of_airports = {'ULLI', 'UUWW', 'USTR'}
        self.url = "ws://localhost:8765"

    async def requester(self):

        while True:
            async with websockets.connect(self.url) as websocket:

                await websocket.send(','.join(self.set_of_airports))

                weather = await websocket.recv()
                time = datetime.datetime.now()

                with open('weather.log', mode='a', encoding='utf-8') as log:
                    log.write('{0}  {1}\n'.format(time.strftime('%H:%M:%S %Y-%m-%d'), weather))

                await asyncio.sleep(10)


wx = WxRequester()
asyncio.run(wx.requester())
