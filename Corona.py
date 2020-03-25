from bs4 import BeautifulSoup
import datetime as dt
import requests
import smtplib
import time

def Get_Cases():
    url = 'https://www.cdc.gov/coronavirus/2019-ncov/cases-updates/cases-in-us.html'

    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
    }

    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")
    data = soup.find('div', {'class': '2019coronavirus-summary'})
    split_data = list(data.stripped_strings)





    return split_data


def send_email():
    server = smtplib.SMTP ('smtp.gmail.com', 587)

    server.starttls()
    server.login('druck1am@gmail.com', 'Poker123!')

    #EMAIL
    recip = 'kmr24@pct.edu', 'druck1am@gmail.com', 'monikadestiny08@gmail.com', 'ryanhadlock1002@gmail.com'
    subject = 'Coronavirus Update'
    body = '\n'.join(Get_Cases())
    message = f'subject: {subject}\n\n{body}'

    server.sendmail('druck1am@gmail.com', recip, message)
    server.quit()


def send_email_at(send_time):
    time.sleep(send_time.timestamp() - time.time())
    send_email()
    print('email sent')

send_time = dt.datetime(2020,3,25,12,0,0)
interval = dt.timedelta(minutes = 1440)

while True:
    send_email_at(send_time)
    send_time = send_time + interval
