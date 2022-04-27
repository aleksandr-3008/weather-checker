Weather-checker client/server app example

This project is an example of how client/server apps work. 
There are two different python files: the first one is 
imitating server's behavior, while the second one makes 
client's requests. This application uses ws protocol on 
port 8765 to share information. You can use this project to
check whether aerodromes that you had
chosen are suitable for the landing or not. 
This app uses https://api.checkwx.com to get all the 
information.
RMK: THIS IS ONLY AN EXAMPLE. METEO-MINIMUMS OF THE
AERODROMES DO NOT FIT REAL ONES.

HOW TO USE (IN FUTURE):

To use this app you should write your unique api key 
from https://api.checkwx.com into 'API_KEY=' row in 
docker-compose.yaml, list the ICAO codes of the 
aerodromes you want in the 'AERODROMES' row
(separating with comma) and run 'docker-compose up' command 
in directory. Two containers will be running together. 
wx_requester_client container will save all the information 
to the weather.log file, which can be seen, while container
is working.(THIS METHOD DOESN'T WORK YET)

WORKS NOW: 

At first, you should write down your api key from 
https://api.checkwx.com (API_KRY) and list the ICAO codes of the 
aerodromes you want (separating with comma) to the 
AERODROMES row in the .sh (Unix) or .ps1(Windows) file
in the directory, depending on which system you are using and 
then run the script. This script will create an API_KEY and an AERODROMES
variable for yor current session. Secondly, you should run
weather_checker.py, which will open the '8765' port.
Then you ought to run weather_requester.py. You will see all the information in
the weather.log

RMK: API_KEY variable is essential. If you don't set AERODROMES
variable, USTR, UUWW, ULLI aerodromes will be used as aerodromes to check

wx_requester.py is a part of an app which imitates client's 
requests to a server. It has set of the aerodromes which are
wanted to be checked on an ability to land there.
wx-requester.py sends a ws-query to the server every 5 minutes,
receives the information and then logs it into the 
weather.log file, which can be checked afterwards. 

wx-checker receives list of the aerodromes to check, sends a http request
to the https://api.checkwx.com, processes json data and forms an answer
to the client.

DOCKER-COMPOSE FIX WILL BE ADDED ADDED SOON
