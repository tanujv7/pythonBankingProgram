#Made By Tanuj Verma
import mysql.connector as mysqc
import time
import keyboard
import sys
print("\U0001F600"*12,"WELCOME TO OUR BANK","\U0001F600"*12)
print("\U0001F600 PROCEED BY PRESSING 'ENTER' FROM YOUR KEYBOARD")
print("\U0001F600 PRESS ESC TO EXIT FROM THE PROGRAM")
print("\U0001F600 Press ENTER To CONTINUE OR PREss ESC TO Quit THE Program:-)")

pstart=False
while True :

    
    try :
        if keyboard.is_pressed("ENTER") :
            print("\U0001F60A STARTING THE PROGRAM....")
            pstart=True
            break
            
        elif keyboard.is_pressed("ESC") :

            print("\U0001F62A QUITTING THE PROGRAM...")
            time.sleep(2)
            print("\U0001F637 QUITTED,BYE")
            sys.exit(0)
            pstart=False
    except :
        break

if pstart==True :
    mydbase=mysqc.connect(host="localhost",user="tanuj",passwd="Tanuj1234",database="") #Database Creation Management Start
    if mydbase.is_connected () :
        None
    mycursor=mydbase.cursor()
    mycursor.execute("show databases;")
    x=mycursor.fetchall()
    dcheck=False   #Creating A Boolean Variable To Check If Database Exists Or Not
    for i in x :
        for y in i :
            if y == "MyBank" :
                dcheck=True
                break
    if dcheck == True :
        None
    else :
        mycursor.execute("create database if not exists MyBank;") #Database Creation Management Over

    mydbase=mysqc.connect(host="localhost",user="tanuj",passwd="Tanuj1234",database="MyBank")
    if mydbase.is_connected () :
        import OBankM as B
        mycursor=mydbase.cursor()

# Table Creation Management Start
    mycursor.execute("Show tables ;") # show All Tables
    tabf=mycursor.fetchall()
    tlist1=[['AA2'],['BAA6'],['CA3'],['LA4'],['PA1'],['RTA5'],['TTA5']]  #taking a list of elements exact similar to Tables
    tlist2=[] #taking an empty list to fill in the fetched elements
    for ix in tlist1 :
        tlist2.append(list(ix)) # Here All The Elements Appended In The List
    ax2=len(tlist1 and tlist2) # calc size of both lists

    dtable=False #Taking A Boolean Variable To Solve The Loop Problem And Further Processes

    for ix2 in range(ax2) : # Comparing Each Element Of Lists
        if tlist1[ix2] in tlist2[ix2] :
            dtable=True
# If dtable is True Then All the Tables Are Already Present

    if dtable==True :
        None

    else : #If Tables Are Not Present Then Tables Are Created Now
        mycursor.execute("create table if not exists PA1 (cname varchar(50),fname varchar(50),mname varchar(50),cdob varchar(10),cmob varchar(11),cadno varchar(12),caddress varchar(100));")
        mycursor.execute("create table if not exists AA2 (cname varchar(50),cmob varchar(11),cacctype Varchar(20),caccno varchar(16) unique key,cpin int(5) unique key,cbalance double(10,2));")
        mycursor.execute("create table if not exists CA3 (cname varchar(50),cmob varchar(11),cpin int(5) unique key,creditcno Varchar(16),cvc int(3) unique key,expdate varchar(8),cbalance double(10,2));")
        mycursor.execute("create table if not exists LA4 (cname varchar(50),caccno varchar(16) ,ltype varchar(50),loan double(10,2),interest varchar(10),ltopay double(10,2),paid double(10,2),status varchar(10) default 'NOT PAID' );")
        mycursor.execute("create table if not exists TTA5 (caccno varchar(16) ,amountr double(10,2),tdate date);")
        mycursor.execute("create table if not exists RTA5 (caccno varchar (16),amountr double(10,2),rdate date);")
        mycursor.execute("create table if not exists BAA6 (cno varchar(20),cname varchar(50),gender varchar(1),fname varchar(50),mname varchar(50),cdob varchar (10),caccno varchar (16) ,cbalance double(10,2),cadno varchar (12),caddress varchar(100),cdate date);")
# Now To Check All The Tables Are Present after Creation
    try :
        mycursor.execute("Show tables ;") # show All Tables
        tabf=mycursor.fetchall()
        tlist1_1=[['AA2'],['BAA6'],['CA3'],['LA4'],['PA1'],['RTA5']]  #taking a list of elements exact similar to Tables
        tlist2_1=[] #taking an empty list to fill in the fetched elements
        for ix_1 in tlist1_1 :
            tlist2_1.append(list(ix_1)) # Here All The Elements Appended In The List
        ax2_1=len(tlist1_1 and tlist2_1) # calc size of both lists
    #Let's Make Sure Everythings Fine

        dtable1=False #Taking A Boolean Variable To Solve The Loop Problem And Further Processes
        for ix2_1 in range(ax2_1) : # Comparing Each Element Of Lists
            if tlist1_1[ix2_1] in tlist2_1 :
                dtable1=True
                   # If dtable is True Then All the Tables Are Already Present

        if dtable1==True :
            None
        elif dtable1==False :
            print("Something's Wrong")

    except :
        None
def pmain() :
            print("\n")
            print("PRESS 1 : TO CREATE AN ACCOUNT")
            print("PRESS 2 : TO DEPOSIT MONEY")
            print("PRESS 3 : TO WITHDRAWL MONEY")
            print("PRESS 4 : TO GET LOAN FROM THE BANK")
            print("PRESS 5 : TO PAY YOUR LOAN AMOUNT OR TO GET INFO ABOUT IT")
            print("PRESS 6 : TO APPLY FOR CREDIT CARD")
            print("PRESS 7 : TO CHECK YOUR TRANSCATION HISTORY")
            print("PRESS 8 : FOR YOUR BANK DETAILS")
            print("PRESS 9 : FOR CUSTOMER SUPPORT")
            print("PRESS 10 : FOR BANK INFO")
            print("PRESS 11 : TO QUIT")
            # HEY GUYS,DON't FORGET TO PRESS ENTER AFTER PRESSING NUMBER
            # I HAVE NO TIME TO AUTOMATE EVERYTHING
            # GOT IT ?
            #ME :- yEAAAAHH
            # EVERYONE :-
            #ME :- DON'T MATTER
            time.sleep(0.5)
            print("\n \n \U0001F604 LETS START:-")
            time.sleep(0.5)
            



            aloop1=1
            while aloop1<=3 :
                try :
                    achoice=int(input("\n \U0001F600 ENTER THE NUMBER REPRESENTING YOUR CHOICE :-"))
                    print("\n")
                    break
                except ValueError :
                    if aloop1==1 :
                        print("\U0001F605 Oops!,Something Went Wrong")
                        print("2 Attempts Left")
                    elif aloop1==2 :
                        print("Please Type Care Fully,Sir/madam")
                        print("1 Attempts Left")
                    elif  aloop1==3 :
                        print("Please Type Carefully This Time,Sir/Madam")
                        print("\U0001F605 No Attempts Left")
                        print("Starting The Program AGain...")
                        time.sleep(1)
                    aloop1+=1
            else :
                print("\n")
                print("\U0001F60A BYE,Again")
                quit

            if achoice==1 :
                B.createacc()
                print("\n")
                pmans=str(input("Do You Want To Continue With The PROGRAM (y/n) or (Y/N) :-"))
                if pmans == "y" or pmans == "Y" :
                    pmain()
                else :
                    print("\n")
                    print("\U0001F607 THANK YOU,FOR YOUR SUPPORT..")
                    print("\U0001F602 BYE","\U0001F600"*5)
                    quit
                    ploop=False
            elif achoice==2 :
                B.depmon()
                print("\n")
                pmans=str(input("Do You Want To Continue With The PROGRAM (y/n) or (Y/N) :-"))
                if pmans == "y" or pmans == "Y" :
                    pmain()
                else :
                    print("\n")
                    print("\U0001F607 THANK YOU,FOR YOUR SUPPORT..")
                    print("\U0001F602 BYE","\U0001F600"*5)
                    quit
                    ploop=False
            elif achoice==3 :
                B.withmon()
                print("\n")
                pmans=str(input("Do You Want To Continue With The PROGRAM (y/n) or (Y/N) :-"))
                if pmans == "y" or pmans == "Y" :
                    pmain()
                else :
                    print("\n")
                    print("\U0001F607 THANK YOU,FOR YOUR SUPPORT..")
                    print("\U0001F602 BYE","\U0001F600"*5)
                    quit
                    ploop=False
            elif achoice==10 :
                B.binfo()
                print("\n")
                pmans=str(input("Do You Want To Continue With The PROGRAM (y/n) or (Y/N) :-"))
                if pmans == "y" or pmans == "Y" :
                    pmain()
                else :
                    print("\n")
                    print("\U0001F607 THANK YOU,FOR YOUR SUPPORT..")
                    print("\U0001F602 BYE","\U0001F600"*5)
                    quit
                    ploop=False
            elif achoice==4 :
                B.getloan()
                print("\n")
                pmans=str(input("Do You Want To Continue With The PROGRAM (y/n) or (Y/N) :-"))
                if pmans == "y" or pmans == "Y" :
                    pmain()
                else :
                    print("\n")
                    print("\U0001F607 THANK YOU,FOR YOUR SUPPORT..")
                    print("\U0001F602 BYE","\U0001F600"*5)
                    quit
                    ploop=False
            elif achoice == 5 :
                B.lpay()
                print("\n")
                pmans=str(input("Do You Want To Continue With The PROGRAM (y/n) or (Y/N) :-"))
                if pmans == "y" or pmans == "Y" :
                    pmain()
                else :
                    print("\n")
                    print("\U0001F607 THANK YOU,FOR YOUR SUPPORT..")
                    print("\U0001F602 BYE","\U0001F600"*5)
                    quit
                    ploop=False
            elif achoice==6 :
                B.credc()
                print("\n")
                pmans=str(input("Do You Want To Continue With The PROGRAM (y/n) or (Y/N) :-"))
                if pmans == "y" or pmans == "Y" :
                    pmain()
                else :
                    print("\n")
                    print("\U0001F607 THANK YOU,FOR YOUR SUPPORT..")
                    print("\U0001F602 BYE","\U0001F600"*5)
                    quit
                    ploop=False
            elif achoice == 7 :
                B.tranhis()
                print("\n")
                pmans=str(input("Do You Want To Continue With The PROGRAM (y/n) or (Y/N) :-"))
                if pmans == "y" or pmans == "Y" :
                    pmain()
                else :
                    print("\n")
                    print("made By Tanuj Verma")
                    print("\U0001F607 THANK YOU,FOR YOUR SUPPORT..")
                    print("\U0001F602 BYE","\U0001F600"*5)
                    quit
                    ploop=False
            elif achoice== 8 :
                B.ccdet()
                print("\n")
                pmans=str(input("Do You Want To Continue With The PROGRAM (y/n) or (Y/N) :-"))
                if pmans == "y" or pmans == "Y" :
                    pmain()
                else :
                    print("\n")
                    print("\U0001F607 THANK YOU,FOR YOUR SUPPORT..")
                    print("\U0001F602 BYE","\U0001F600"*5)
                    quit
                    ploop=False
            elif achoice == 9 :
                B.csupp()
                print("\n")
                pmans=str(input("Do You Want To Continue With The PROGRAM (y/n) or (Y/N) :-"))
                if pmans == "y" or pmans == "Y" :
                    pmain()
                else :
                    print("\n")
                    print("\U0001F607 THANK YOU,FOR YOUR SUPPORT..")
                    print("\U0001F602 BYE","\U0001F600"*5)
                    quit
                    ploop=False
            elif achoice == 11 :
                print("\n")
                print("\U0001F607 THANK YOU,FOR YOUR SUPPORT..")
                print("\U0001F602 BYE","\U0001F600"*5)
                quit
                
            else :
                print("\U0001F605 SORRY SIR,INVALID CHOICE :-(")


#Table Creation Management Over
if pstart==True :
    ploop=True
    pmain()
        

