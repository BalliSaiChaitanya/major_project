from hash_fun import decrypt
def match_donors_recipient():
    d=[]
    r=[]
    flg=1
    file = open('ledger_donors.txt','r')
    lines = file.readlines()
    for i in lines:
        dec=decrypt(i)
        st=dec.split("*")
        d.append(st)  #append decrypted data list to main list
    file = open('ledger_recipient.txt','r')
    lines = file.readlines()
    for i in lines:
        dec=decrypt(i)
        st=dec.split("*")
        r.append(st)
    print("\n ----->Searching Finding Hits <--------\n")
    for i in range(len(d)):
        organ=d[i][0]
        for j in range(len(r)):
            reporg=r[j][0]
            if organ == reporg:
                flg=0
                print("\n--->Found a match for a recipient: ")
                print("Donating "+d[i][1]+"'s "+organ+" to "+r[j][1])
                print("\nSharing Data To Hospital Server")
                print("Sharing "+d[i][1]+"'s"+" information to "+r[j][1])
    if(flg):
        print("\n***** No Hits found *****\n")


    return 0

match_donors_recipient()