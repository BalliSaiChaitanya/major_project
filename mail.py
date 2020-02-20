import smtplib

fromaddr = "sc.balli22@gmail.com"  
toaddrs  = "schaitanya.balli@gmail.com"  
msg = 'Spam email Test'  

username = 'sc.balli22'  
password = '#'

server = smtplib.SMTP('smtp.gmail.com', 587)  
server.ehlo()
server.starttls()
server.login(username, password)  
server.sendmail(fromaddr, toaddrs, msg)  
server.quit()
