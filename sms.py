from twilio.rest import Client
import pyowm
import time

while(True):
        owm=pyowm.OWM('7a6c2f736e3fe03a91def1a486e2b49a')
        observation=owm.weather_at_place('Delhi,IN')
        w=observation.get_weather()
        humidity=w.get_humidity()
        
        print(humidity)
        
        acc_sid="ACf25181487f9c996adb6e3b146d157ad5"
        auth_tok="bdb257515273319afa145bf0d24a9b3d"
        client=Client(acc_sid,auth_tok)
        if(humidity>70):
            message=client.messages.create(body="Humidity exceeds set level",
                                           to="+919618261525",
                                           from_=" +13394997596")
            print(message.sid)
        else:
            message=client.messages.create(body="humidity is below set level",
                                           to="+919618261525",
                                           from_=" +13394997596")
            print(message.sid)
        time.sleep(2)
