import smtplib
import ssl


def sendEmail(message):
    host = 'smtp.gmail.com'
    port = 465
    username = 'dnero543@gmail.com'
    password = 'vccxddpnzrwybvrm'
    receive = 'dnero543@gmail.com'
    context = ssl.create_default_context()



    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receive, message)


