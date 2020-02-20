from hash_fun import encrypt,decrypt
from match import match_donors_recipient
import os
def ency(node1,node2):
    pass
def donor_details():
    print("#-------> Enter Donor Details <------#")
    d_details=[]
    name=input("Enter Name: ")
    mobi=input("Enter Contact number: ")
    address=input("Enter address: ")
    email=input("Enter email: ")
    blood=input("Enter blood group: ")
    age=input("Enter Age: ")
    gender=input("Enter gender: ")
    organ=input("Organ to donate: ")
    d_details.append(organ)
    d_details.append(name)
    d_details.append(mobi)
    d_details.append(address)
    d_details.append(email)
    d_details.append(blood)
    d_details.append(age)
    d_details.append(gender)
    

    str_details="*"
    str_details=str_details.join(d_details)
    if(os.stat("./ledger_donors.txt").st_size == 0):
        e_details=encrypt(str_details)
        text_file = open("ledger_donors.txt", "a")
        text_file.write(e_details+"\n")
    else:
        e_details=encrypt(str_details)
        text_file = open("ledger_donors.txt", "a")
        text_file.write(e_details+"\n")



def recipient_details():
    print("#-------> Enter recpient Details <------#")
    r_details=[]
    name=input("Enter Name: ")
    mobi=input("Enter Contact numbe: r")
    address=input("Enter address: ")
    email=input("Enter email: ")
    blood=input("Enter blood group: ")
    age=input("Enter Age: ")
    gender=input("Enter gender: ")
    organ=input("Which Organ needed: ")
    r_details.append(organ)
    r_details.append(name)
    r_details.append(mobi)
    r_details.append(address)
    r_details.append(email)
    r_details.append(blood)
    r_details.append(age)
    r_details.append(gender)
    

    str_details="*"
    str_details=str_details.join(r_details)
    if(os.stat("./ledger_recipient.txt").st_size == 0):
        e_details=encrypt(str_details)
        text_file = open("./ledger_recipient.txt", "a")
        text_file.write(e_details+"\n")
    else:
        e_details=encrypt(str_details)
        text_file = open("./ledger_recipient.txt", "a")
        text_file.write(e_details+"\n")
    

def match_organs():
    x= match_donors_recipient()
    """with open('ledger_donors') as f:
        dry_details = f.readline()
        print(dry_details)
        samp=decrypt(dry_details)
        print(samp)"""

def check_connection():
    pass

def status():
    pass

def options():
    print("1: Enter Donor's Details ")
    print("2: Enter Recipient details ")
    print("3: show matched patients ")
    print("4: check connection and verification ")
    print("5: status ")
    ip=int(input(""))

    #swithc function
    if(ip==1):
        donor_details() 
    elif(ip==2):
        recipient_details()
    elif(ip==3):
        match_organs()
    elif(ip==4):
        check_connection()
    elif(ip==5):
        status()

options()

    
