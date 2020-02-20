import smtplib

def email_send(details,r_name,r_email,organ):
    fromaddr = "chaindonars20@gmail.com"  
    toaddrs  = r_email 
    SUBJECT="Alert! We have found a donor for "+organ
    TEXT= "Hello "+r_name+",\n"+"Hope you are doing well, we have found a donor for "+organ+"\nand the donors Details are: \n"+"   Name= "+details[1]+"\n   Mobile no= "+details[2]+"\n   Address= "+details[3]+"\n   Age= "+details[6]
    
    msg = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)  

    username = 'chaindonars20'  
    password = 'chain2020'
    server = smtplib.SMTP('smtp.gmail.com', 587)  
    server.ehlo()
    server.starttls()
    server.login(username, password)  
    server.sendmail(fromaddr, toaddrs, msg)  
    server.quit()


