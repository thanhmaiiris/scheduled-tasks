import datetime as dt
import random
import smtplib
import os
WEEKLY_SENDING_DAY = 0
to_mail = "student232616@ptnk.edu.vn"
my_mail = os.environ.get("MY_EMAIL")
password = os.environ.get("MY_PASSWORD")


def check_weekday():
    now = dt.datetime.now()
    weekday = now.weekday()
    print(weekday)
    if weekday == WEEKLY_SENDING_DAY:
        return True
    else:
        return False

with open("quotes.txt") as file:
    quotes = file.readlines()
    print(quotes)

def get_random_quote():
    random_quote = random.choice(quotes)
    print(random_quote)
    return random_quote

if check_weekday() == True:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_mail, password=password)
        connection.sendmail(
            from_addr=my_mail,
            to_addrs=to_mail,
            msg=f"Subject: Quote of the day\n\n{get_random_quote()}"
        )



