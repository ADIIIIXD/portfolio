import smtplib, ssl

host = "smtp.gmail.com"
port = 465

username = "tbrown101299@gmail.com"
password = "hvkzerqnelurtbbc"

receiver = "vikaditya119@gmail.com"
message = """\
Subject: Testing
This email is part of the testing procedure for the script
"""

context = ssl.create_default_context()

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)