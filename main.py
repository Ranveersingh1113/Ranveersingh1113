import os

import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
API_KEY='555814c377a5abb74259921f5e4630fc'
account_sid = 'AC146df627f1d4c1a633e5ce4be4c793cd'
auth_token = '27f2c8eb1e85eab7fbb41b044cff7b29'
parameters={'lat':18.520760,'lon':73.855410,'appid':API_KEY,'cnt':4}
response=requests.get(url='http://api.openweathermap.org/data/2.5/forecast',params=parameters)
response.raise_for_status()
data=response.json()
for i in range(data['cnt']):
    if data['list'][i]['weather'][0]['id']<700:
        proxy_client=TwilioHttpClient()
        proxy_client.session.proxies={'https':os.environ['https_proxy']}
        client=Client(account_sid,auth_token,http_client=proxy_client)
        message = client.messages.create(body="It might rain,carry an umbrella☔",
            from_='+14123143707',
            to='+917987568051')
        break
# noinspection PyUnboundLocalVariable
print(message.status)