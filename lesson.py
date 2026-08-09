def sending_mail():
    import smtplib
    my_email = "thanhmaiiris2407@gmail.com"
    password = "zxsi tzhj htbz xxoa"

    # connection = smtplib.SMTP("smtp.gmail.com")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # encryption
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="student232616@ptnk.edu.vn",
            msg="Subject: HELLO\n\nThis is the body of my email"
        )
    # connection.close() with with, you dont need to close

def date_time_module():
    import datetime as dt

    now = dt.datetime.now()
    year = now.year #month, day, second
    print(now)
    print(year)
    day_of_week = now.weekday() #starts from 0, sun is 6
    print(day_of_week)

    dob = dt.datetime(year = 2008, month = 7, day = 24)
    print(dob)

def monday_quote_challenge():
    import datetime as dt
    import random
    import smtplib
    WEEKLY_SENDING_DAY = 0
    my_mail = "thanhmaiiris2407@gmail.com"
    to_mail = "student232616@ptnk.edu.vn"
    password = "zxsi tzhj htbz xxoa"

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



