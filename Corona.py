from bs4 import BeautifulSoup
import datetime as dt
import requests
import smtplib
import time

def currentPrice():
    url = 'https://www.cdc.gov/coronavirus/2019-ncov/cases-updates/cases-in-us.html'

    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
    }

    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'lxml')
    cases = soup.find("td", text="Total cases").find_next_sibling("td").text

    return cases

def send_email():
    cases = currentPrice()
    email_user = 'druck1am@gmail.com'
    server = smtplib.SMTP ('smtp.gmail.com', 587)
    server.starttls()
    server.login('druck1am@gmail.com', 'Poker123!')

    #EMAIL
    message = 'Total Cases: ' + str(cases)
    server.sendmail(email_user, email_user, message)
    server.quit()

def send_email_at(send_time):
    time.sleep(send_time.timestamp() - time.time())
    send_email()
    print('email sent')

first_email_time = dt.datetime(2020,3,24,3,0,0)
interval = dt.timedelta(minutes=2*60)

send_time = first_email_time
while True:
    send_email_at(send_time)
    send_time = send_time + interval


