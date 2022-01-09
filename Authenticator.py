from smtplib import SMTP

def Authenticate(username, password, host_id, host_port):
    c1 = False
    c2 = False
    test_obj = SMTP(host_id, host_port)

    if test_obj.ehlo():
        print("Connection with Host Success!!")
        c1 = True
    else:
        print("Connection Error!!")
        c1 = False
    test_obj.starttls()

    try:
        test_obj.login(username, password)
        c2 = True
    except:
        print("Login Error")
        c2 = False

    if c1 and c2:
        return True
    else:
        return False
