from twilio.rest import Client
import pyowm
import time

while(True):
        owm=pyowm.OWM('--Weather report key---')
        observation=owm.weather_at_place('Delhi,IN')
        w=observation.get_weather()
        humidity=w.get_humidity()
        
        print(humidity)
        
        acc_sid="--account sid-----"
        auth_tok="---authentication token----"
        client=Client(acc_sid,auth_tok)
        if(humidity>70):
            message=client.messages.create(body="Humidity exceeds set level",
                                           to="+91--receiver number",
                                           from_=" +twilio number")
            print(message.sid)
        else:
            message=client.messages.create(body="humidity is below set level",
                                           to="+91 ---receiver number",
                                           from_=" +twilio number")
            print(message.sid)
        time.sleep(2)
