import datetime as dt
import time
import smtplib
import codecs

def email_send(details,r_name,r_email,organ):
    
    fromaddr = "chaindonars@gmail.com"
    password = 'dzzjtkzjoajxypsh'  
    toaddrs  = r_email 
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(fromaddr, password)
    s="Alert! We have found a donor for "+organ
    sub=s.replace("\x0a", " ")
    txt= "Hello "+r_name+",\n"+"Hope you are doing well, we have found a donor for "+organ+"\nand the donors Details are: \n"+" Name= "+details[1]+"\n Mobile no= "+details[2]+"\n Address= "+details[3]+"\n Age= "+details[6]
    spaced_message = txt.replace("\x0a", " ")
    msg = 'Subject: {}\n\n{}'.format(sub, spaced_message)  
    message = 'Subject: {}\n\n{}'.format(sub,msg)
    server.sendmail(fromaddr, toaddrs, message)
    server.quit()
    print("Success: Email sent!")



"""
def email_send(details,r_name,r_email,organ):
    fromaddr = "chaindonars@gmail.com"  
    toaddrs  = r_email 
    SUBJECT="Alert! We have found a donor for "+organ
    TEXT= "Hello "+r_name+",\n"+"Hope you are doing well, we have found a donor for "+organ+"\nand the donors Details are: \n"+" Name= "+details[1]+"\n Mobile no= "+details[2]+"\n Address= "+details[3]+"\n Age= "+details[6]
    
    msg = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)  
    username = 'chaindonars'  
    
    server = smtplib.SMTP('smtp.gmail.com', 587)  
    server.BodyEncoding = 'utf-8'
    server.ehlo()
    server.starttls()
    server.login(username, password)  
    server.sendmail(fromaddr, toaddrs, msg)  
    server.quit()"""