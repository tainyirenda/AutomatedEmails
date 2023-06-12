import datetime as dt
import smtplib
import random

MY_EMAIL = "taiestellenyirenda@gmail.com"
MY_PASSWORD = "opeaurjwrabckotd"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="taiestellenyirenda@icloud.com",
                            msg=f"Subject: Monday Motivation\n\n{quote}")
