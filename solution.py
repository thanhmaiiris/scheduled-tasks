import datetime
import pandas
import random
import smtplib
today_tuple = (datetime.datetime.now().month , datetime.datetime.now().day)
data = pandas.read_csv('birthdays.csv')

birthdays_dict = {(data_row.month, data_row.day): data_row for (index,data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as f:
        content = f.read()
        new_content = content.replace("[NAME]",birthday_person["name"])
    with smtplib.SMTP("SMTP.gmail.com") as connection:
        connection.starttls()
        connection.login("thanhmaiiris2407@gmail.com", "zxsi tzhj htbz xxoa")
        connection.sendmail(
            from_addr="thanhmaiiris2407",
            to_addrs = birthday_person["email"],
            msg = f"Subject: HAPPY BIRThday!\n\n{new_content}"
        )

