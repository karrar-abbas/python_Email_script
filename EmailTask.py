import subprocess
import ssl
import smtplib
"""
The script only works with Gmail accounts

Allow less secure apps: Must be enabled from account settings
"""


# ----------------------pinging -----------------------

Host=input("Enter The Host's Address Or IP : ")
ping=subprocess.run(["ping",Host], capture_output=True)
result=str(ping.stdout,'utf-8')
print(result)

# ---------------------Sending Email -------------------

port = 465
smtp_server = "smtp.gmail.com"
context = ssl.create_default_context()
server = smtplib.SMTP_SSL("smtp.gmail.com", port, context=context)

# -------------------------------------------------------

sender_email = input("Enter Your Email :") # Login To Your Email
pwd = input("Enter your password : ")
login = False
while login == False :
    try:
        print(" logging ...")
        server.login(sender_email, pwd)
        login= True
        print(" login Done")
    except:
        print('---- Incorrect Username or Password ----')
        sender_email = input("Enter Your Email :")
        pwd = input("Enter your password : ")

#------------------------------------------------------------
receiver_email = input("Enter Receiver Email To Send Results :")
print("---- Input Just In English ----")
msg_sub=input(" Message's Subject :")
message = """\
Subject: {}
    
Result of ping Your {} :
{}
""".format(msg_sub,Host,result)
server.sendmail(sender_email, receiver_email, message,)
print("--- Message Sent ---")