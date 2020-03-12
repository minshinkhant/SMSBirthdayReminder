# sending birthday reminder message to your phone number
#with twilio trial account

import time
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

proxy_client = TwilioHttpClient()
proxy_client.session.proxies = {'https': os.environ['https_proxy']}

account_sid = '[your_account_sid]'
auth_token = '[AuthToken]'
client = Client(account_sid, auth_token, http_client=proxy_client)


def checkTodayBirthdays():
    file_name = open('text.txt', 'r')
    today = time.strftime('%m%d')
    flag = 0
    for line in file_name:
        if today in line:
            line = line.split(' ')
            flag = 1
            # twilio api calls will now work from behind the proxy:
            message = client.messages.create(
                    from_='new_ph_number_we_created',
                    to='your_phone_number',
                    body=f"Today is {line[1]} {line[2]} birthday!!"

                )
            print(message.sid)
    if flag == 0:
        no_birthday = client.messages.create(
            from_='new_ph_number_we_created',
            to='your_phone_number',
            body="There is no birthday Today!!!"
        )
        print(no_birthday.sid)


if __name__ == '__main__':
    checkTodayBirthdays()