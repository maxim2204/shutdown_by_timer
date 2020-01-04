import smtplib
def Go():
    email = 'shutdown@taurl.space'
    password = 'prostocod123'

    server = smtplib.SMTP('smtp.yandex.ru', 587)
    server.ehlo() #
    server.starttls()
    server.login(email, password)

    dest_email = 'maxim.timaev05@gmail.com'
    subject = 'Your Bot'
    email_text = 'Dear taurl, your "BMW" was shutdown'
    message = 'From: %s\nTo: %s\nSubject: %s\n\n%s' % (email, dest_email, subject, email_text)

    server.set_debuglevel(1) #
    server.sendmail(email, dest_email, message)
    server.quit()