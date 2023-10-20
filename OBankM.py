#REASONABLE WAY.. PLEASE ENJOY...)
import mysql.connector as mysqc #Connecting To The DataBase
import string # fOR VALIDIFICATION
import random # FOR GENERATING PINS AND ACCOUNT NUMBERS
from captcha.audio import AudioCaptcha # FOR AUDIO TYPE CAPTCHA
from captcha.image import ImageCaptcha # FOR IMAGE TYPE CAPTCHA
import matplotlib.pyplot as mplib # FOR IMAGE SHOW,ALSO CAN BE USED TO SHOW THE GRAPH BETWEEN (DEOSITED VS WITHDRAWL) "I WILL THINK ABOUT IT.."
import matplotlib.image as mpimage # FOR IMAGE SHOW..
from playsound import playsound # FOR PLAYING CAPTCHA SOUND
import time # FOR THE COMPUTER TO SLEEP
from datetime import date # FOR DATE MANAGING STUFF
from tabulate import tabulate # FOR SHOWING TABLES
mydbase=mysqc.connect(host="localhost",user="tanuj",passwd="Tanuj1234",database="MyBank")
if mydbase.is_connected () :
    mycursor=mydbase.cursor()
    mycursor.execute("Set AUTOCOMMIT=0 ;")
    #Cursor Object Created

empty=0

def intch(inx) :
    if type(inx) == int :
        return True
    else :
        return False
def strch(srx) :
    if type(srx) == str :
        return True
    elif srx == 0 and srx != str :#This Is For Bank Account Number Selection ErrorCounter Measure
        return False
try :
    def captcha() :
        print()
        print("\U0001F600 Now You Have To Clear The CAPTCHA :-")
        print("What Type Of Captcha You Would Like To Go For:-")
        print("1.For Image Type CAPTCHA")
        print("2.For Audio Type CAPTCHA")
        print("\n")
        captin=int(input("\U0001F600 What Type OF Captcha Would You Like To GO For:-")) #Input For Selecting Captcha Type
        if type(captin) == int :
            if captin==1 : #If Selected Option 1
                randig=random.randint(1000,9999) ##Creating Random 4 Digit Number For The Captcha
                print("\n\U0001F600 You Have Chosen Image Type Captcha Filling:-")
                image=ImageCaptcha() #Creating Image Object
                image.write(str(randig),"capimg.png") #Writing On To The Image Object
                imagsh=mpimage.imread("capimg.png") #Image Showing Program With The Help Of Matplotlib Module.. Starting.. #Here Reading The Image
                imgplot=mplib.imshow(imagsh) #To Ready To Show The Image
                time.sleep(1) #Wait For 1 Second
                print()
                print("\U0001F600 Now Showing Your Captcha Image...")
                time.sleep(1) #Wait For One Second
                mplib.show() #Showing The Image

                capans1=int(input("\n \U0001F600 Enter The Captcha Code Please :-")) #Input For The Captcha Code
                capansv=intch(capans1)
                if capansv == True :
                    if capans1==randig :
                        return True
                else :
                    print("Please Enter A Valid Choice..Or Enter A Valid Input .i.e An Integer")
        

                    
        elif captin==2 : #If Chosen Image Type Captcha Verification
                randig1=random.randint(1000,9999) #Creating A Random 4 Digit Number For Captcha
                audio=AudioCaptcha() #Creating Audio Object
                audio.write(str(randig1),"capaud.wav") #Writing On To The Image Object
                print("\U0001F600 Now Playing Your Audio Captcha")
                print("\U0001F600 Please Listen To The Captcha Audio Carefully")
                time.sleep(1) #Waiting For 1 Sec
                print("Loading...")
                time.sleep(1)
                playsound("capaud.wav") #Playing Sound..Of Captcha
                capans2=int(input("\U0001F600 Enter Your Audio Captcha Code Carefully :-")) #Input The Captcha Code
                capansv1 = intch(capans2) 
                if capansv1 == True :
                    if capans2==randig1 : #If Successfully Verified
                        return True
        else :
            print("Please Enter AN Integer Value \U0001F600")
                
                

                
        

    def csupn(csupin): # Function To Verify Name
        csc1="select cname from AA2 where cname=%s;"
        csc2=(csupin,)
        mycursor.execute(csc1,csc2)
        cscdat1=mycursor.fetchall()
        for cscx in cscdat1 :
            if cscx[0]== csupin :
                return True
    def csupm(csupin) : # Function To Verify Mobile Number
        csc3="select cmob from AA2 where cmob=%s;"
        csc4=(csupin,)
        mycursor.execute(csc3,csc4)
        cscdat2=mycursor.fetchall()
        for cscx in cscdat2 :
            if cscx[0]==csupin :
                return True
    def csupacc(csupin) : # Function To Verify Account Number
        csc5="select caccno from AA2 where caccno=%s;"
        csc6=(csupin,)
        mycursor.execute(csc5,csc6)
        cscdat3=mycursor.fetchall()
        for cscx in cscdat3 :
            if cscx[0]==csupin :
                return True
    def csuppi(csupin) : # Function To Verify PIN Number
        csc7="select cpin from AA2 where cpin=%s;"
        csc8=(int(csupin),)
        mycursor.execute(csc7,csc8)
        cscdat4=mycursor.fetchall()
        for cscx in cscdat4 :
            if cscx[0]==csupin :
                return True
            else :
                return False
        

    #Account creation Beginning
    def createacc(): #Account Creation Function
        print("\U0001F607 Welcome To The Account Creation Setup:-")
        print("\n\U0001F600 Account Types:-")
        print("1.CHECKING ACCOUNT")
        print("2.SAVINGS ACCOUNT")
        print("3.INVVESTMENT ACCOUNT")
        aloop1=1
        while aloop1<=3 : #Loop To Enter Correct Choice Or Number
            try :
                atypein=int(input("\n\U0001F600 Enter The Number Representing Your Desired Account Type :-"))
                if atypein > 3 or atypein == 0 :
                    print("\nPlease Enter An Valid Integer Answer :-)\n")
                    createacc()
                else :
                    break
            except ValueError : #Handling The ValueError
                if aloop1==1 : #Loop To Tell About Attempts And Security
                    print("\n\U0001F605 Oops!,Something Went Wrong")
                    print("\n Probably,You Have Entered A String..Please Type An Right Integer Value")
                    print("\n2 Attempts Left")
                elif aloop1==2 :
                    print("\n\U0001F605 Please Type Care Fully,Sir/madam")
                    print("\n1 Attempts Left")
                elif  aloop1==3 :
                    print("\n\U0001F605 Please Type Carefully This Time,Sir/Madam")
                    print("\U0001F605 No Attempts Left")
                    print("\nStarting The Account Creation Again...")
                    time.sleep(1)
                aloop1+=1
        else :
            createacc() #After 3 Attempts , Function Called Again

        if atypein==1 : #Account Type Assignment To A Variable
            actype="Checking"
            
        elif atypein==2 :
            actype="Savings"
            
        elif atypein==3 :
            actype="Investment"
        
        #Now,Enter Data For Your Account
        def checkN1():
            astr1=str(1234567890) #Contain All The Natural Number As String
            astr2=string.punctuation        #Conatins All The Strings
            a1in=str(input("\n\U0001F600 Enter Your Name Sir/Madam:-")) #Input For The Customer's Name
            bcheck1=list(map(lambda char : char in (astr1+astr2),a1in)) #Checking ALl The elements And mapping it And Converting It Into The List
            if any(bcheck1) :   #Loop For Entering A Valid Name
                print("\n\U0001F605 Please Enter A Valid Name:")
                return checkN1() #If Any Element In bcheck1 present Then Function Called Again
            else :
                return a1in #The OutPut
        a1in=checkN1()
        #Receiving The Output

        

        def checkN2():
            astr1=str(1234567890)   #Contain All The Natural Number As String
            astr2=string.punctuation      #Conatins All The Strings
            a2in=str(input("\n\U0001F600 Enter Your  Father's Name:-"))      #Input For The Customer's Father Name
            bcheck1=list(map(lambda char : char in (astr1+astr2),a2in))     #Checking ALl The elements And mapping it And Converting It Into The List
            if any(bcheck1) :           #Loop For Entering A Valid Name
                print("\n\U0001F605 Please Enter A Valid Name:")
                return checkN2()        #If Any Element In bcheck1 present Then Function Called Again
            else :
                return a2in #The Output
        a2in=checkN2()

        def checkN3():
            astr1=str(1234567890)       #Contain All The Natural Number As String
            astr2=string.punctuation        #Conatins All The Strings
            a3in=str(input("\n\U0001F600 Enter Your Mother's Name:-"))               #Input For The Customer's Mother Name
            bcheck1=list(map(lambda char : char in (astr1+astr2),a3in))     #Checking ALl The elements And mapping it And Converting It Into The List
            if any(bcheck1) :
                print("\n\U0001F605 Please Enter A Valid Name:")     #Loop For Entering A Valid Name
                return checkN3()        #If Any Element In bcheck1 present Then Function Called Again
            else :
                return a3in #The Output
        a3in=checkN3()
        

        def checkN5():
            gen=None
            genq=str(input("\n\U0001F600 Dear Sir/Madam,Please Enter Your GENDER (M/F):-")) #Getting The Input For Gender
            if genq=="M" or genq=="m" :
                gen="M"
            elif genq=="F" or genq=="f" :
                gen="F"
            else :
                print("\n\U0001F605 Please Enter Valid Answer (M/N) :-)")
                checkN5()
        gen=checkN5()
                
                

        def checkN4():
            astr1=string.ascii_letters #Contains All The Letters
            a4in=str(input("\n\U0001F600 Enter Your Date Of Birth :-")) #Input For Date Of BIRTH                                                                                                                                            (This Section Needs Improvement)
            bcheck1=list(map(lambda char : char in (astr1),a4in)) ##Checking ALl The elements And mapping it And Converting It Into The List
            if any(bcheck1) :
                print("\n\U0001F605 Please Enter A Valid Date") ##Loop For Entering A Valid Name
                return checkN4()    ##If Any Element In bcheck1 present Then Function Called Again
            else :
                return a4in#The Output
        a4in=checkN4()      #Receiving Thre OutPut
        
        a6in=str(input("\n\U0001F600 Enter Your Aadhar Number :-")) #Customer's Aadhar Number                                                                                                                                       (This Section Needs Improvement)
        while len(a6in) !=12 :                                                  #Loop To Enter Valid 12 Digit Aadhar Number
            print("\n\U0001F605 Please,Enter Your's And Valid Aadhar Number")
            a6in=str(input("\n\U0001F600 Enter Your Aadhar Number :-"))
        a7in=str(input("\n\U0001F600 Dear SIR/MADAM,Please Enter Your Address:-"))

        a5in=str(input("\n\U0001F600 Enter Your Mobile Number :-"))
        while len(a5in)!=10 and len(a5in)!=11 and (a5in).isdigit() == False:                     #Loop To Enter Valid Mobile Number Of Either 10 Digit Or 11 Digit
            print("\n\U0001F605 Please Enter Valid Mobile Number")
            a5in=str(input("\n\U0001F600 Enter Your Mobile Number :-"))
            
        
        print("\n\U0001F600 Well Done \U0001F600")
        print("\n\U0001F600 70% Account Established")
        time.sleep(1)
        print("\n\U0001F600 Dear Sir/Madam,You Have To Pay Inital Amount To Succesfully Activate Your Account")
        print("\n\U0001F600 Kindly Pay Money (2000 Or More Rupees) As Your Inital Amount")
        def iniap():
           #Function To Pay The Initial Amount
            iniam=str(input("\n\U0001F600 Enter How Much Money You Want To Pay:-")) #Input Amount Of Money
            if iniam.isdigit() : #Checking If The Amount Is In Digits Or Alphabets..
                        
                while int(iniam) < 2000 : #Loop For The Money Or Amount Limit
                            
                    print("\n\U0001F605 Please pay 2000 Rupees or More")
                    iniam=int(input("\n\U0001F600 Enter How Much Money You Want To Pay:-"))
                   #Returning Output
            else :
                print("\n\U0001F605 Please Enter A Valid Amount:-")
                return iniap() #If Invalid Function Callled Again
            return iniam

        iniam=iniap() #Receiving The Output
        
        if int(iniam)>=2000 : #Now To Make Sure Everything's Gone Right This Far

                capans1=captcha()
                if capans1==True :
                    time.sleep(0.8)
                    print("\U0001F600 Now,You Will Get Your Account Number:-")
                    time.sleep(0.8)
                    print("\U0001F600 Please Note Down The Account Number AND PIN CODE SomeWhere Very SAfe")
                    time.sleep(1) #Wait For 1 Sec
                    accno=random.randint(10000,99999) #Creating A Random 5 Digit Number For Account Number
                    def accnox() :
                        accnon=random.randint(10000,99999) #Creating A Random 5 Digit Account Number
                        accomx1="select caccno from AA2 where caccno=%s;"
                        accomx2=(accnon,)
                        mycursor.execute(accomx1,accomx2)
                        accdat=mycursor.fetchall()
                        if mycursor.rowcount != 0 :
                            for acx in accdat :
                                if acx[0] == accnon :
                                    print("SORRY,ACCOUNT NUMBER EXISTED,FETCHING NEW ONE...")
                                    return accnox()
                                else :
                                    return accnon
                        else  :
                            return accnon
                    accno=accnox()
                    print("\n\U0001F600 Your ACCOUNT NUMBER IS:-",accno)
                    
                    # Inserted Account Number In The Table:
                    print("\n\U0001F600 Now Getting Your PIN Code..")
                    time.sleep(1)
                    pinno=random.randint(1000,9999) #Creating A Random 4 Digit Number For Account
                    print("\n\U0001F600 Your PIN Number is :-",pinno)
                    
                    #Inserted Pin Number In The Account:-
                    print("\n\U0001F600 Congratulations!,Your Account Is Ready")

                    ccch=True
                
                else:
                    print()
                    print("\U0001F605 It Was Wrong")
                    ccch=False
                    
        if ccch== True :
            aldatsav1="insert into PA1(cname,fname,mname,cdob,cmob,cadno,caddress) values(%s,%s,%s,%s,%s,%s,%s)" #Inserting Into Table PA1
            aldatsav2=(a1in,a2in,a3in,a4in,a5in,a6in,a7in)
            mycursor.execute(aldatsav1,aldatsav2)
            aldatsav3="insert into AA2 (cname,cmob,cacctype,caccno,cpin,cbalance) values(%s,%s,%s,%s,%s,%s)" #Inserting Into Table AA2
            aldatsav4=(a1in,a5in,actype,accno,pinno,iniam)
            mycursor.execute(aldatsav3,aldatsav4)
            altdatsav5="insert into RTA5(rdate) values(curdate());" # Inserting Into Table RTA5
            mycursor.execute(altdatsav5)
            mydbase.commit() # Committing ALL The Insertions

        else :
            print("\n")
            print("Something Went Wrong...)")
        

    def depmon() :
        print("\n\U0001F607 Here,You Will Deposit Your Money")
        print("Loading...")
        time.sleep(1)
        dacc0=str(input("\n\U0001F607 Dear SIR/MADAM,Please ENTER Your NAME :-")) # Getting Name
        depnamchk=csupn(dacc0) #Name Verification
        if depnamchk == True : # If True Then All This Down Below :-)
            dacc1=str(input("\n\U0001F600 Enter Your Account Number Here:-")) #Account And PIN CHECKING,I Had'nt Made Functions While Making This ,So This Is Direct ( _-_ ) + Going To Fetch DATA
            acchk1=csupacc(dacc1) #ACCOUNT NUMBER VERIFICATION
            if acchk1 == True :
                dpinno1=int(input("\n\U0001F600 Enter Your Account PIN Code:-"))
                pinchk1=csuppi(dpinno1) # PIN NUMBER VERIFICATION
                print(pinchk1)
                if pinchk1 == True :
                    xc1=("Select * from AA2 where caccno=%s and cpin=%s")
                    xc2=(dacc1,dpinno1)
                    mycursor.execute(xc1,xc2)
                    dacinfo=mycursor.fetchall()
                
                    if mycursor.rowcount==0 : # If Nothing , Then This ..
                        print("\n\U0001F605 SORRY,NO RESULT FOUND")
                    else : # Else ALL THIS
                        for xcheckac in dacinfo : #Getting The Output
                            print("\n\U0001F607 Your Current Balance Is",xcheckac[5],"Rupees")
                            moninp=int(input("\n\U0001F600 Enter How Much Money Do You Want To Deposit:-")) #Getting The Money Input Value To Deposit
                            monv=intch(moninp)
                            if monv == True :
                                admon=moninp+xcheckac[5] # Adding The Total Money That Was Before And Depoisted Now
                                xc3="update  AA2 set cbalance =%s where caccno=%s" #Updating The DATABASE
                                xc4=(admon,dacc1)
                                mycursor.execute(xc3,xc4)
                                mydbase.commit()
                                if mycursor.rowcount==1 : # IF SUCCESSFULLY UPDATED,THEN THIS
                                    print("\n\U0001F600 The Transaction Is Successfull")
                                    xc1=("Select * from AA2 where caccno=%s and cpin=%s")
                                    xc2=(dacc1,dpinno1)
                                    mycursor.execute(xc1,xc2)
                                    dacinfo1=mycursor.fetchall()
                                    print("\n\U0001F607 Now,Your Current Balance In Your Account Is:-",([xcheckac1[5] for xcheckac1 in dacinfo1] ),end=" "),print("Rupees") #Printing ALL About Updated MONEY
                                    altdatsav1="insert into TTA5(caccno,amountr,tdate) values(%s,%s,curdate());" # Here Its For The TRANSACTION STUFF
                                    altdatsav2=(dacc1,moninp)
                                    mycursor.execute(altdatsav1,altdatsav2)
                                    if mycursor.rowcount > 0 : # It's USUAL AS ALWAYS (HEHEHE)
                                        mydbase.commit()
                                    else : #ElSES ALL AHEAD
                                        
                                        print("\n\U0001F605 The Transaction HISTORY Couldn't Be SAVED")
                            else :
                                print("\n\U0001F605 SORRY,SOMETHING WENT WRONG")
                else :
                    print("\n\U0001F605 SORRY,PLEASE CHECK YOUR ACCOUNT'S PIN AND TRY AGAIN")
                
            else :
                print("\n\U0001F605 Check Your ACCOUNT NUMBER AND THEN TRY AGAIN :-)")
            
                            
        else :
            print("\n\U0001F605 SORRY,PLEASE CHECK YOUR NAME AND TRY AGAIN")
            
        

    def withmon() : #Function Or Program To Deposit Money
        print("\n\U0001F607 Hi,Please Enter The Following Details To With Draw Money:-")
        print("LOADING...")
        time.sleep(1) # Sleeping Or Resting For 1 Seconds { Computer :- Hey,Tanuj Please Let Me Sleep For One Sec,And It Will All Be ALLRIGHT..It Will FEEL GOOD TOO | Me :- Okay..(AS You Wish) CAN I SLEEP TOO ?) | Computer :- NA , You Have Work To Do
        Wacc0=str(input("\n\U0001F607 Dear SIR/MADAM,Please ENTER Your NAME :-")) # Getting The Name..
        repnamchk=csupn(Wacc0) # Name Verification
        if repnamchk == True : # If True Then All This
            wacc1=str(input("\n\U0001F600 Enter Your Account Number Here:-")) # ALL The Verification + Getting To Withdraw..
            acchk1=csupacc(wacc1)
            if acchk1 == True :
                xc1=("Select * from AA2 where caccno=%s;")
                xc2=(wacc1,)
                mycursor.execute(xc1,xc2)
                dacinfo=mycursor.fetchall()
                for tempx in dacinfo :
                    print("\n\U0001F607 Your Current Balance is",tempx[5],"Rupees") #GIVING THE CURRENT BALANCE
                    #TO ADDD CAPTCHA HERE :____
                capans=captcha()
                if capans == True :
                    print("\U0001F600 NOW")
                    wpinno1=int(input("\n\U0001F600 Enter Your Account Pin Code:-")) # PIN AND ACCOUNT NUMBER TO FETCH DETAILS
                    xc1=("Select * from AA2 where caccno=%s and cpin=%s")
                    xc2=(wacc1,wpinno1)
                    mycursor.execute(xc1,xc2)
                    dacinfo=mycursor.fetchall()
                    if mycursor.rowcount==0 : #If Nothing Then This
                        print("\n\U0001F605 SORRY,SOMETHING WENT WRONG,PLEASE CHECK YOUR CREDENTIALS AND TRY AGAIN")
                    else : #Otherwise This
                        for xcheckac3 in dacinfo :
                            if mycursor.rowcount==0 : #Extra Checking
                                print("\n\U0001F605 Something Went Wrong:-")
                            else :
                                for tempx0 in dacinfo :
                                    None
                                if tempx0[5] < 2000 : # If Money In The Account Is Less Than 2000,Then This :-)
                                    print("\n\U0001F605 You Have No Sufficient Balance To Withdraw :-( ")
                                else : # Otherwise ALL OKAY,THis..
                                    wmon=int(input("\n\U0001F600 Enter How Much Money You Would Like To With Draw:-"))
                                    if wmon < 2000 :
                                        print("\n\U0001F605 Sorry!,You Don't Have Enough Balance To Withdraw Any Money")
                                    elif wmon < 500 :
                                        print("\n\U0001F605 Sorry!,You Cannot Withdraw This Small Amount,Please Withdraw Money About 2000+")
                                    else :
                                        for tempx2 in dacinfo : # Now Updating The Database
                                            submon=tempx2[5]-wmon
                                            xc3="update  AA2 set cbalance =%s where caccno=%s"
                                            xc4=(submon,wacc1)
                                            mycursor.execute(xc3,xc4)
                                            mydbase.commit()
                                    
                                        print(wmon,"Rupees of Amount Has Been debited From Your Account Number",tempx2[3],".If It Wasn't You,Please Contact The Bank") #Now Printing ALL The Information
                                        xcy1="select cbalance from AA2 where caccno=%s "
                                        xcy2=(wacc1,)
                                        mycursor.execute(xcy1,xcy2)
                                        dacinfo2=mycursor.fetchall()
                                        for tempx3 in dacinfo :
                                            print("\U0001F600 Now,Your Current Account Balance Is :-",submon,"Rupees") # Printing Current Balance..
            else :
                print("\n\U0001F605 SORRY,PLEASE CHECK YOUR ACCOUNT NUMBER AND THEN TRY AGAIN")
            
        else :
            print("\n\U0001F605 SORRY,Please CHECK Your NAME AND Try AGAIN")
        alrsav1="insert into RTA5(caccno,amountr,rdate) values(%s,%s,curdate());" # SAVING DATA FOR TRANSACTION DETAILS
        alrsav2=(wacc1,wmon)
        mycursor.execute(alrsav1,alrsav2)
        if mycursor.rowcount > 0 :
            mydbase.commit()
        else :
            print("\n\U0001F605 The Transaction HISTORY Couldn't Be SAVED") #IF SOMETHING WENT WRONG THEN THIS WILL SHOW
                    

    def hl() : # FUNCTION FOR THE DETAILS ABOUT HOME LOANS OR HL
        print("For HOME LOANS:-")
        print("\nFor LOANS 1LAKH To 10LAKH RUPEES")
        print("\tINTEREST=2% WITH TIME 4 YEARS")
        print("\nFOR LOANS ABOVE 10 LAKH AND UP TO 1 CRORE")
        print("\tINTEREST=3% WITH TIME 6 YEARS")
        print("\nFor LOANS ABOVE 1 CRORE AND UPTO 50 CRORE")
        print("\tINTEREST = 5% WITH TIME 15 YEARS")
    def sl() : #FUNCTION FOR THE DETAILS ABOUT STUDENT LOAN OR SL
        print("For STUDENT LOANS :-")
        print("\nFor LOANS 50000 To 1LAKH RUPEES")
        print("\tINTEREST=2% WITH TIME 4 YEARS")
        print("\nFor LOANS ABOVE 10 LAKHS AND UPTO 5 CRORE")
        print("\tINTEREST = 5% WITH TIME 15 YEARS")
    def pl() : # FUNCTION FOR THE DETAILS ABOUT PERSONAL LOANS OR PL
        print("For PERSONAL LOANS :-")
        print("\nFor LOANS 1000 To 50000 RUPEES")
        print("\tINTEREST=1% WITH TIME 4 YEARS")
        print("\nFOR LOANS ABOVE 50000  AND UP TO 5 LAKHS")
        print("\tINTEREST=2% WITH TIME 6 YEARS")
        print("\nFor LOANS ABOVE 5 LAKHS AND UPTO 50 LAKHS")
        print("\tINTEREST = 3% WITH TIME 8 YEARS")
        print("\nFor LOANS ABOVE 50 LAKHS AND UPTO 1 CRORE")
        print("\tINTEREST=4% WITH TIME 10 YEARS")
        print("\nFor LOANS ABOVE 1 CRORE AND UPTO 10 CRORE")
        print("\tINTEREST=5% WITH TIME 12 YEARS")
    def al() : # FUCNTION FOR THE DETAILS ABOUT AUTO LOANS OR AL
        print("For AUTO LOANS:-")
        print("\nFor LOANS 1LAKH To 10LAKH RUPEES")
        print("\tINTEREST=2% WITH TIME 4 YEARS")
        print("\nFOR LOANS ABOVE 10 LAKH AND UP TO 1 CRORE")
        print("\tINTEREST=3% WITH TIME 6 YEARS")
        print("\nFor LOANS ABOVE 1 CRORE AND UPTO 50 CRORE")
        print("\tINTEREST = 5% WITH TIME 15 YEARS")
    def smbl() : # FUNCTIONS FOR THE DETAILS ABOUT SMALL BUSINESS LOAN
        print("For SMALL BUSINESS LOANS:-")
        print("\nFor LOANS 1LAKH To 10LAKH RUPEES")
        print("\tINTEREST=2% WITH TIME 4 YEARS")
        print("\nFOR LOANS ABOVE 10 LAKH AND UP TO 1 CRORE")
        print("\tINTEREST=3% WITH TIME 6 YEARS")
        print("\nFor LOANS ABOVE 1 CRORE AND UPTO 50 CRORE")
        print("\tINTEREST = 5% WITH TIME 15 YEARS")
        
    def lcalcs(amount, interest, times, lcg1,lcg2,ltype) : #FUNCTION FOR THE CALCULATION OF LOAN..INTEREST,TOTAL AMOUNT TO PAY OR TOTAL LOAN TO PAY,STUFF LIKE THAT
        # This Is The Calender Program
        curdate=date.today() # GETTING THE CURRENT DATE
        curyear=curdate.year #2020
        ydays=0 # VARIABLE
        if curyear % 4 == 0 : # TAKING CARE OF THE LEAP YEAR
            monx=[jan,feb,mar,apr,may,jun,jul,aug,sep,octo,nov,dec]=[30,29,30,31,30,31,30,31,30,31,30,31]
            ydays=366
        else :
            monx=[jan,feb,mar,apr,may,jun,jul,aug,sep,octo,nov,dec]=[30,28,30,31,30,31,30,31,30,31,30,31]
            ydays=365
        
        imdaily=interest/100/365 * amount #INTEREST AMOUNT ON DAILY BASIS
        immonthly=imdaily* monx[curdate.month - 1] # INTEREST AMOUNT ON MONTHLY BASIS
        linnfosavv1 = "insert into LA4 (cname,caccno,ltype,loan,interest,ltopay) values(%s,%s,%s,%s,%s,%s);"
        linnfosavv2 = (lcg1, lcg2, ltype, amount, interest,amount + imdaily * ydays)
        mycursor.execute(linnfosavv1, linnfosavv2)
        if mycursor.rowcount == 0 :
            print("\n\U0001F605 SORRY SOMETHING WENT WRONG,PLEASE CHECK YOUR CREDENTIALS")
        else :
            imyearly= imdaily * ydays # INTEREST AMOUNT FOR YEARS
            print("\n\U0001F600 Your Daily Interest Amount Is :-",int(imdaily),"Rupees")
            print("\n\U0001F600 Your Monthly Interest Amount Is:-",int(immonthly),"Rupees")
            print("\n\U0001F600 Your Annual Interest Amount Is :-",int(imyearly),"Rupees")
            mydbase.commit() #Committed The Data

    def loanredch(caccno) :
        xlr1="select * from la4 where caccno = %s ;"
        xlr2=(caccno,)
        mycursor.execute(xlr1,xlr2)
        datxred=mycursor.fetchone()
        for x in datxred :
            if x[0] == caccno :
                return False
            else :
                return True

        

        
        
        
        
    def getloan() : # THIS SECTION NEEDS IMPROVEMENT
        print("\n\U0001F607 Dear SIR/MADAM ,YOU ARE HERE TO GET YOUR LOAN :-) ")
        print("\n\U0001F607 OK,LET's GET STARTED")
        print("\n\U0001F607 Here's SOME INFO :-")
        print("1.MORTGAGES/HOME LOANS")
        print("2.STUDENT LOANS")
        print("3.PERSONAL LOANS")
        print("4.AUTO LOANS")
        print("5.SMALL BUSINESS LOANS")
        xfans = False
        lcg1=str(input("\n\U0001F600 DEAR SIR/MADAM,Please ENTER Your NAME:-"))
        lcgchk1=csupn(lcg1)
        if lcgchk1 == True :
            lcg2=str(input("\n\U0001F600 Enter YOUR ACCOUNT NUMBER:-"))
            lcgchk2=csupacc(lcg2)
            impch=loanredch(lcg2)
            if impch == True :
                if lcgchk2 == True :
                    lcg3=int(input("\n\U0001F600 DEAR SIR/MADAM ENTER THE NUMBER OF YOUR DESIRED LOAN TYPE:-"))
                    ltype=None
                    if lcg3==1 :
                        ltype="HOME LOAN"
                        print("\n\U0001F607 YOU HAVE SELECTED HOME LOANS") #HOME LOANS STARTED
                        print("\n\U0001F600 HERE's SOME INFO ABOUT IT:-")
                        hl()
                        ltype="HOME LOAN"
                        lcg4=int(input("\n\U0001F600 DEAR SIR/MADAM,How MUCH LOAN DO YOU WANT :-"))
                        l1=100000
                        l10=1000000
                        c1=10000000
                        c50=500000000
                        if lcg4 < l1 :
                            print("\n\U0001F605 Please ENTER VALID AMOUNT OF MONEY AS MENTIONED:-")
                            xfans = False
                        elif lcg4 >= l1 and lcg4 <= l10 :
                            print("\n\U0001F600 You ARE PROCEEDING WITH THE LOAN OF :-",lcg4)
                            print("\n\U0001F600 Your TOTAL INTEREST WOULD BE :- 2 %") ; interest=2
                            print("\n\U0001F600 Your TOTAL INSTALLMENT TIME IS :- 4 Years") ; times=4
                            print("\n\U0001F600 NOW THE PIN AND VERIFICATION PROCESS IS AHEAD..\n PLEASE CLEAR THEM AND THEN YOUR LOAN WLL BE APPROVED..")
                            time.sleep(1)
                            capout=captcha()
                            if capout==True :
                                lcg5=int(input("\n\U0001F600 DEAR SIR/MADAM,PLEASE ENTER YOUR ACCOUNT PIN CODE.."))
                                lcinget1="select cpin from AA2 where caccno=%s;"
                                lcinget2=(lcg2,)
                                mycursor.execute(lcinget1,lcinget2)
                                mylcdat=mycursor.fetchone()
                                for xlc in mylcdat :
                                    if xlc == lcg5 :
                                        print("\n\U0001F600 ADDING THE MONEY TO YOUR BANK ACCOUNT...")
                                        time.sleep(1)
                                        lccom1="update AA2 set cbalance=cbalance+%s where caccno=%s"
                                        lccom2=(lcg4,lcg2)
                                        mycursor.execute(lccom1,lccom2)
                                        print("\n\U0001F600 CONGRATULATIONS,LOAN AMOUNT SUCCESSFULL ADDED TO YOUR ACCOUNT BALANCE:--)")
                                        print("\n\U0001F600 ENJOY..")
                                        xfans = True
                                    else :
                                        print("\n\U0001F605 SOMETHING WENT WRONG..")
                                        xfans = False
                            else :
                                print("\n\U0001F605 SOMETHONG WENT WRONG")
                                xfans = False
                        elif lcg4 > l10 and lcg4 <=c1 :
                            print("\n\U0001F600 You ARE PROCEEDING WITH THE LOAN OF :-",lcg4)
                            print("\n\U0001F600 Your TOTAL INTEREST WOULD BE :- 3 %") ; interest=3
                            print("\n\U0001F600 Your TOTAL INSTALLMENT TIME IS :- 6 Years") ; times=6
                            print("\n\U0001F600 NOW THE PIN AND VERIFICATION PROCESS IS AHEAD..\n PLEASE CLEAR THEM AND THEN YOUR LOAN WLL BE APPROVED..")
                            time.sleep(1)
                            capout=captcha()
                            if capout==True :
                                lcg5=int(input("\n\U0001F600 DEAR SIR/MADAM,PLEASE ENTER YOUR ACCOUNT PIN CODE.."))
                                lcinget1="select cpin from AA2 where caccno=%s;"
                                lcinget2=(lcg2,)
                                mycursor.execute(lcinget1,lcinget2)
                                mylcdat=mycursor.fetchone()
                                for xlc in mylcdat :
                                    if xlc == lcg5 :
                                        print("\n\U0001F600 ADDING THE MONEY TO YOUR BANK ACCOUNT...")
                                        time.sleep(1)
                                        lccom1="update AA2 set cbalance=cbalance+%s where caccno=%s"
                                        lccom2=(lcg4,lcg2)
                                        mycursor.execute(lccom1,lccom2)
                                        print("\n\U0001F600 CONGRATULATIONS,LOAN AMOUNT SUCCESSFULL ADDED TO YOUR ACCOUNT BALANCE:--)")
                                        print("\n\U0001F600 ENJOY..")
                                        xfans = True
                                    else :
                                        print("\n\U0001F605 SOMETHING WENT WRONG..")
                                        xfans = False
                            else :
                                print("\n\U0001F605 CAPTCHA VERIFICATION FAILED")
                                xfans = False


                        elif lcg4 > c1 and lcg4 <=c50 :
                            print("\n\U0001F600 You ARE PROCEEDING WITH THE LOAN OF :-",lcg4)
                            print("\n\U0001F600 Your TOTAL INTEREST WOULD BE :- 5 %") ; interest=5
                            print("\n\U0001F600 Your TOTAL INSTALLMENT TIME IS :- 15 Years") ; times=15
                            print("\n\U0001F600 NOW THE PIN AND VERIFICATION PROCESS IS AHEAD..\n PLEASE CLEAR THEM AND THEN YOUR LOAN WLL BE APPROVED..")
                            time.sleep(1)
                            capout=captcha()
                            if capout==True :
                                lcg5=int(input("\n\U0001F600 DEAR SIR/MADAM,PLEASE ENTER YOUR ACCOUNT PIN CODE.."))
                                lcinget1="select cpin from AA2 where caccno=%s;"
                                lcinget2=(lcg2,)
                                mycursor.execute(lcinget1,lcinget2)
                                mylcdat=mycursor.fetchone()
                                for xlc in mylcdat :
                                    if xlc == lcg5 :
                                        print("\n\U0001F600 ADDING THE MONEY TO YOUR BANK ACCOUNT...")
                                        time.sleep(1)
                                        lccom1="update AA2 set cbalance=cbalance+%s where caccno=%s"
                                        lccom2=(lcg4,lcg2)
                                        mycursor.execute(lccom1,lccom2)
                                        print("\n\U0001F600 CONGRATULATIONS,LOAN AMOUNT SUCCESSFULL ADDED TO YOUR ACCOUNT BALANCE:--)")
                                        print("\n\U0001F600 ENJOY..")
                                        xfans = True
                                    else :
                                        print("\n\U0001F605 SOMETHING WENT WRONG..")
                                        xfans = False
                            
                            else :
                                print("\n\U0001F605 SOMETHING WENT WRONG...")    #HOME LOAN ENDED
                                xfans = False
                        #mydbase.commit()
                        #lcalcs(lcg4,interest,times,lcg2)
                            
                            
                            
                        
                    elif lcg3==2 :              #STUDENT LOANS STARTED
                        ltype="STUDENT LOAN"
                        
                        print("\n\U0001F607 YOU HAVE SELECTED STUDENT LOANS")
                        print("\n\U0001F607 HERE's SOME INFO ABOUT IT:-")
                        sl()
                        ltype="STUDENT LOAN"
                        lcg4=int(input("\n\U0001F600 DEAR SIR/MADAM,How MUCH LOAN DO YOU WANT :-"))
                        k50=50000
                        l1=100000
                        l10=1000000
                        c5=50000000
                        if lcg4 < k50 :
                            print("\n\U0001F605 Please ENTER VALID AMOUNT OF MONEY AS MENTIONED:-")
                        elif lcg4 >= k50 and lcg4 <= l1 :
                            print("\n\U0001F600 You ARE PROCEEDING WITH THE LOAN OF :-",lcg4)
                            print("\n\U0001F600 Your TOTAL INTEREST WOULD BE :- 2 %") ; interest=2
                            print("\n\U0001F600 Your TOTAL INSTALLMENT TIME IS :- 4 Years") ; times=4
                            print("\n\U0001F600 NOW THE PIN AND VERIFICATION PROCESS IS AHEAD..\n PLEASE CLEAR THEM AND THEN YOUR LOAN WLL BE APPROVED..")
                            time.sleep(1)
                            capout=captcha()
                            if capout==True :
                                lcg5=int(input("\U0001F600 DEAR SIR/MADAM,PLEASE ENTER YOUR ACCOUNT PIN CODE.."))
                                lcinget1="select cpin from AA2 where caccno=%s;"
                                lcinget2=(lcg2,)
                                mycursor.execute(lcinget1,lcinget2)
                                mylcdat=mycursor.fetchone()
                                for xlc in mylcdat :
                                    if xlc == lcg5 :
                                        print("\n\U0001F600 ADDING THE MONEY TO YOUR BANK ACCOUNT...")
                                        time.sleep(1)
                                        lccom1="update AA2 set cbalance=cbalance+%s where caccno=%s"
                                        lccom2=(lcg4,lcg2)
                                        mycursor.execute(lccom1,lccom2)
                                        print("\n\U0001F600 CONGRATULATIONS,LOAN AMOUNT SUCCESSFULL ADDED TO YOUR ACCOUNT BALANCE:--)")
                                        print("\n\U0001F600 ENJOY..")
                                        xfans = True
                                    else :
                                        print("\n\U0001F605 SOMETHING WENT WRONG..")
                                        xfans = False
                            else :
                                print("\n\U0001F605 SOMETHING WENT WRONG...")
                                xfans = False
                        elif lcg4 >l10 and lcg4 <= c5 :
                            print("\n\U0001F600 You ARE PROCEEDING WITH THE LOAN OF :-",lcg4)
                            print("\n\U0001F600 Your TOTAL INTEREST WOULD BE :- 3 %") ; interest=3
                            print("\n\U0001F600 Your TOTAL INSTALLMENT TIME IS :- 6 Years") ; times=6
                            print("\n\U0001F600 NOW THE PIN AND VERIFICATION PROCESS IS AHEAD..\n PLEASE CLEAR THEM AND THEN YOUR LOAN WLL BE APPROVED..")
                            time.sleep(1)
                            capout=captcha()
                            if capout==True :
                                lcg5=int(input("\n\U0001F600 DEAR SIR/MADAM,PLEASE ENTER YOUR ACCOUNT PIN CODE.."))
                                lcinget1="select cpin from AA2 where caccno=%s;"
                                lcinget2=(lcg2,)
                                mycursor.execute(lcinget1,lcinget2)
                                mylcdat=mycursor.fetchone()
                                for xlc in mylcdat :
                                    if xlc == lcg5 :
                                        print("\n\U0001F600 ADDING THE MONEY TO YOUR BANK ACCOUNT...")
                                        time.sleep(1)
                                        lccom1="update AA2 set cbalance=cbalance+%s where caccno=%s"
                                        lccom2=(lcg4,lcg2)
                                        mycursor.execute(lccom1,lccom2)
                                        print("\n\U0001F600 CONGRATULATIONS,LOAN AMOUNT SUCCESSFULL ADDED TO YOUR ACCOUNT BALANCE:--)")
                                        print("\n\U0001F600 ENJOY..")
                                        xfans = True
                                    else :
                                        print("\n\U0001F605 SOMETHING WENT WRONG..")
                                        xfans = False
                            else :
                                print("\n\U0001F605 SOMETHING WENT WRONG...") #STUDENT LOANS ENDED
                                xfans = False
                        #mydbase.commit()
                        #lcalcs(lcg4,interest,times,lcg2)
                            
                    elif lcg3==3 :              #PERSONAL LOANS STARTED
                        ltype="PERSONAL LOAN"
                        print("\n\U0001F607 YOU HAVE SELECTED PERSONAL LOANS")
                        print("\n\U0001F607 HERE's SOME INFO ABOUT IT:-")
                        pl()
                        ltype="PERSONAL LOAN"
                        lcg4=int(input("\n\U0001F600 DEAR SIR/MADAM,How MUCH LOAN DO YOU WANT :-"))
                        k50=50000
                        l5=500000
                        l50=5000000
                        c1=10000000
                        c10=100000000
                        if lcg4 < 1000 :
                            print("\n\U0001F600 Please ENTER VALID AMOUNT OF MONEY AS MENTIONED:-")
                        elif lcg4 >= 1000 and lcg4 <= k50 :
                            print("\n\U0001F600 You ARE PROCEEDING WITH THE LOAN OF :-",lcg4)
                            print("\n\U0001F600 Your TOTAL INTEREST WOULD BE :- 1 %") ; interest=1
                            print("\n\U0001F600 Your TOTAL INSTALLMENT TIME IS :- 4 Years") ; times=4
                            print("\n\U0001F600 NOW THE PIN AND VERIFICATION PROCESS IS AHEAD..\n PLEASE CLEAR THEM AND THEN YOUR LOAN WLL BE APPROVED..")
                            time.sleep(1)
                            capout=captcha()
                            if capout==True :
                                lcg5=int(input("\n\U0001F600 DEAR SIR/MADAM,PLEASE ENTER YOUR ACCOUNT PIN CODE.."))
                                lcinget1="select cpin from AA2 where caccno=%s;"
                                lcinget2=(lcg2,)
                                mycursor.execute(lcinget1,lcinget2)
                                mylcdat=mycursor.fetchone()
                                for xlc in mylcdat :
                                    if xlc == lcg5 :
                                        print("\n\U0001F600 ADDING THE MONEY TO YOUR BANK ACCOUNT...")
                                        time.sleep(1)
                                        lccom1="update AA2 set cbalance=cbalance+%s where caccno=%s"
                                        lccom2=(lcg4,lcg2)
                                        mycursor.execute(lccom1,lccom2)
                                        print("\n\U0001F600 CONGRATULATIONS,LOAN AMOUNT SUCCESSFULL ADDED TO YOUR ACCOUNT BALANCE:--)")
                                        print("\n\U0001F600 ENJOY..")
                                        xfans = True
                                    else :
                                        print("\n\U0001F605 SOMETHING WENT WRONG..")
                                        xfans = False


                            print("\n\U0001F605 CAPTCHA VERIFICATION FAILED")
                            xfans = False
                        elif lcg4 > k50 and lcg4 <=l5 :
                            print("\n\U0001F600 You ARE PROCEEDING WITH THE LOAN OF :-",lcg4)
                            print("\n\U0001F600 Your TOTAL INTEREST WOULD BE :- 2 %") ; interest = 2
                            print("\n\U0001F600 Your TOTAL INSTALLMENT TIME IS :- 6 Years") ; times = 6
                            print("\n\U0001F600 NOW THE PIN AND VERIFICATION PROCESS IS AHEAD..\n PLEASE CLEAR THEM AND THEN YOUR LOAN WLL BE APPROVED..")
                            time.sleep(1)
                            capout=captcha()
                            if capout==True :
                                lcg5=int(input("\n\U0001F600 DEAR SIR/MADAM,PLEASE ENTER YOUR ACCOUNT PIN CODE.."))
                                lcinget1="select cpin from AA2 where caccno=%s;"
                                lcinget2=(lcg2,)
                                mycursor.execute(lcinget1,lcinget2)
                                mylcdat=mycursor.fetchone()
                                for xlc in mylcdat :
                                    if xlc == lcg5 :
                                        print("\n\U0001F600 ADDING THE MONEY TO YOUR BANK ACCOUNT...")
                                        time.sleep(1)
                                        lccom1="update AA2 set cbalance=cbalance+%s where caccno=%s"
                                        lccom2=(lcg4,lcg2)
                                        mycursor.execute(lccom1,lccom2)
                                        print("\n\U0001F600 CONGRATULATIONS,LOAN AMOUNT SUCCESSFULL ADDED TO YOUR ACCOUNT BALANCE:--)")
                                        print("\n\U0001F600 ENJOY..")
                                        xfans = True
                                    else :
                                        print("\n\U0001F605 SOMETHING WENT WRONG..")
                                        xfans = False
                                    
                            
                            else :
                                print("\n\U0001F605 SOMETHING WENT WRONG...")
                                xfans = False
                        elif lcg4 > l5 and lcg4 <=l50 :
                            print("\n\U0001F600 You ARE PROCEEDING WITH THE LOAN OF :-",lcg4)
                            print("\n\U0001F600 Your TOTAL INTEREST WOULD BE :- 3 %") ; interest=3
                            print("\n\U0001F600 Your TOTAL INSTALLMENT TIME IS :- 8 Years") ; times=8
                            print("\n\U0001F600 NOW THE PIN AND VERIFICATION PROCESS IS AHEAD..\n PLEASE CLEAR THEM AND THEN YOUR LOAN WLL BE APPROVED..")
                            time.sleep(1)
                            capout=captcha()
                            if capout==True :
                                lcg5=int(input("\n\U0001F600 DEAR SIR/MADAM,PLEASE ENTER YOUR ACCOUNT PIN CODE.."))
                                lcinget1="select cpin from AA2 where caccno=%s;"
                                lcinget2=(lcg2,)
                                mycursor.execute(lcinget1,lcinget2)
                                mylcdat=mycursor.fetchone()
                                for xlc in mylcdat :
                                    if xlc == lcg5 :
                                        print("\n\U0001F600 ADDING THE MONEY TO YOUR BANK ACCOUNT...")
                                        time.sleep(1)
                                        lccom1="update AA2 set cbalance=cbalance+%s where caccno=%s"
                                        lccom2=(lcg4,lcg2)
                                        mycursor.execute(lccom1,lccom2)
                                        print("\n\U0001F600 CONGRATULATIONS,LOAN AMOUNT SUCCESSFULL ADDED TO YOUR ACCOUNT BALANCE:--)")
                                        print("\n\U0001F600 ENJOY..")
                                        xfans = True
                                    else :
                                        print("\n\U0001F605 SOMETHING WENT WRONG..")
                                        xfans = False
                                    
                            
                            else :
                                print("\n\U0001F605 SOMETHING WENT WRONG...")
                        elif lcg4 > l50 and lcg4 <= c1 :
                            print("\n\U0001F600 You ARE PROCEEDING WITH THE LOAN OF :-",lcg4)
                            print("\n\U0001F600 Your TOTAL INTEREST WOULD BE :- 4 %") ; interest=4
                            print("\n\U0001F600 Your TOTAL INSTALLMENT TIME IS :- 10 Years") ; times=10
                            print("\n\U0001F600 NOW THE PIN AND VERIFICATION PROCESS IS AHEAD..\n PLEASE CLEAR THEM AND THEN YOUR LOAN WLL BE APPROVED..")
                            time.sleep(1)
                            capout=captcha()
                            if capout==True :
                                lcg5=int(input("\n\U0001F600 DEAR SIR/MADAM,PLEASE ENTER YOUR ACCOUNT PIN CODE.."))
                                lcinget1="select cpin from AA2 where caccno=%s;"
                                lcinget2=(lcg2,)
                                mycursor.execute(lcinget1,lcinget2)
                                mylcdat=mycursor.fetchone()
                                for xlc in mylcdat :
                                    if xlc == lcg5 :
                                        print("\n\U0001F600 ADDING THE MONEY TO YOUR BANK ACCOUNT...")
                                        time.sleep(1)
                                        lccom1="update AA2 set cbalance=cbalance+%s where caccno=%s"
                                        lccom2=(lcg4,lcg2)
                                        mycursor.execute(lccom1,lccom2)
                                        print("\n\U0001F600 CONGRATULATIONS,LOAN AMOUNT SUCCESSFULL ADDED TO YOUR ACCOUNT BALANCE:--)")
                                        print("\n\U0001F600 ENJOY..")
                                        xfans = True
                                    else :
                                        print("\nU0001F605 SOMETHING WENT WRONG..")
                                        xfans = False
                                    
                            
                            else :
                                print("\n\U0001F605 SOMETHING WENT WRONG...")
                                xfans = False

                        elif lcg4 > c1 and lcg4 <=c10 :
                            print("\n\U0001F600 You ARE PROCEEDING WITH THE LOAN OF :-",lcg4)
                            print("\n\U0001F600 Your TOTAL INTEREST WOULD BE :- 5 %") ; interest=5
                            print("\n\U0001F600 Your TOTAL INSTALLMENT TIME IS :- 12 Years") ; times=12
                            print("\n\U0001F600 NOW THE PIN AND VERIFICATION PROCESS IS AHEAD..\n PLEASE CLEAR THEM AND THEN YOUR LOAN WLL BE APPROVED..")
                            time.sleep(1)
                            capout=captcha()
                            if capout==True :
                                lcg5=int(input("\n\U0001F600 DEAR SIR/MADAM,PLEASE ENTER YOUR ACCOUNT PIN CODE.."))
                                lcinget1="select cpin from AA2 where caccno=%s;"
                                lcinget2=(lcg2,)
                                mycursor.execute(lcinget1,lcinget2)
                                mylcdat=mycursor.fetchone()
                                for xlc in mylcdat :
                                    if xlc == lcg5 :
                                        print("\n\U0001F600 ADDING THE MONEY TO YOUR BANK ACCOUNT...")
                                        time.sleep(1)
                                        lccom1="update AA2 set cbalance=cbalance+%s where caccno=%s"
                                        lccom2=(lcg4,lcg2)
                                        mycursor.execute(lccom1,lccom2)
                                        print("\n\U0001F600 CONGRATULATIONS,LOAN AMOUNT SUCCESSFULL ADDED TO YOUR ACCOUNT BALANCE:--)")
                                        print("\n\U0001F600 ENJOY..")
                                        xfans = True
                                    else :
                                        print("\n\U0001F605 SOMETHING WENT WRONG..")
                                        xfans = False
                                    
                            
                            else :
                                print("\n\U0001F605 SOMETHING WENT WRONG...") #PERSONAL LOANS ENDED
                                xfans = False
                        #mydbase.commit()
                        #lcalcs(lcg4,interest,times,lcg2)
                            
                        
                    elif lcg3==4 : # AUTO LOANS STARTED
                        ltype="AUTO LOAN"
                        print("\n\U0001F607 YOU HAVE SELECTED AUTO LOANS")
                        print("\n\U0001F607 HERE's SOME INFO ABOUT IT:-")
                        al()
                        ltype="AUTO LOAN"
                        lcg4=int(input("\n\U0001F600 DEAR SIR/MADAM,How MUCH LOAN DO YOU WANT :-"))
                        l1=100000
                        l10=1000000
                        c1=10000000
                        c50=500000000
                        if lcg4 < l1 :
                            print("\n\U0001F605 Please ENTER VALID AMOUNT OF MONEY AS MENTIONED:-")
                        elif lcg4 >= l1 and lcg4 <= l10 :
                            print("\n\U0001F600 You ARE PROCEEDING WITH THE LOAN OF :-",lcg4)
                            print("\n\U0001F600 Your TOTAL INTEREST WOULD BE :- 2 %") ; interest=2
                            print("\n\U0001F600 Your TOTAL INSTALLMENT TIME IS :- 4 Years") ; times =4
                            print("\n\U0001F600 NOW THE PIN AND VERIFICATION PROCESS IS AHEAD..\n PLEASE CLEAR THEM AND THEN YOUR LOAN WLL BE APPROVED..")
                            time.sleep(1)
                            capout=captcha()
                            if capout==True :
                                lcg5=int(input("\n\U0001F600 DEAR SIR/MADAM,PLEASE ENTER YOUR ACCOUNT PIN CODE.."))
                                lcinget1="select cpin from AA2 where caccno=%s;"
                                lcinget2=(lcg2,)
                                mycursor.execute(lcinget1,lcinget2)
                                mylcdat=mycursor.fetchone()
                                for xlc in mylcdat :
                                    if xlc == lcg5 :
                                        print("\n\U0001F600 ADDING THE MONEY TO YOUR BANK ACCOUNT...")
                                        time.sleep(1)
                                        lccom1="update AA2 set cbalance=cbalance+%s where caccno=%s"
                                        lccom2=(lcg4,lcg2)
                                        mycursor.execute(lccom1,lccom2)
                                        print("\n\U0001F600 CONGRATULATIONS,LOAN AMOUNT SUCCESSFULL ADDED TO YOUR ACCOUNT BALANCE:--)")
                                        print("\n\U0001F600 ENJOY..")
                                        xfans = True
                                    else :
                                        print("\n\U0001F605 SOMETHING WENT WRONG..")
                                        xfans = False

                            else :
                                print("\n\U0001F605 SOMETHING WENT WRONG...")
                        elif lcg4 > l10 and lcg4 <= c1 :
                            print("\n\U0001F600 You ARE PROCEEDING WITH THE LOAN OF :-",lcg4)
                            print("\n\U0001F600 Your TOTAL INTEREST WOULD BE :- 3 %") ; interest=3
                            print("\n\U0001F600 Your TOTAL INSTALLMENT TIME IS :- 6 Years") ; times = 6
                            print("\n\U0001F600 NOW THE PIN AND VERIFICATION PROCESS IS AHEAD..\n PLEASE CLEAR THEM AND THEN YOUR LOAN WLL BE APPROVED..")
                            time.sleep(1)
                            capout=captcha()
                            if capout==True :
                                lcg5=int(input("\n\U0001F600 DEAR SIR/MADAM,PLEASE ENTER YOUR ACCOUNT PIN CODE.."))
                                lcinget1="select cpin from AA2 where caccno=%s;"
                                lcinget2=(lcg2,)
                                mycursor.execute(lcinget1,lcinget2)
                                mylcdat=mycursor.fetchone()
                                for xlc in mylcdat :
                                    if xlc == lcg5 :
                                        print("\n\U0001F600 ADDING THE MONEY TO YOUR BANK ACCOUNT...")
                                        time.sleep(1)
                                        lccom1="update AA2 set cbalance=cbalance+%s where caccno=%s"
                                        lccom2=(lcg4,lcg2)
                                        mycursor.execute(lccom1,lccom2)
                                        print("\n\U0001F600 CONGRATULATIONS,LOAN AMOUNT SUCCESSFULL ADDED TO YOUR ACCOUNT BALANCE:--)")
                                        print("\n\U0001F600 ENJOY..")
                                        xfans = True
                                    else :
                                        print("\n\U0001F605 SOMETHING WENT WRONG..")
                                        xfans = False
                                    
                            
                            else :
                                print("\nU0001F605 SOMETHING WENT WRONG...")
                                xfans = False

                        elif lcg4 > c1 and lcg4 < c50 :
                            print("\n\U0001F600 You ARE PROCEEDING WITH THE LOAN OF :-",lcg4)
                            print("\n\U0001F600 Your TOTAL INTEREST WOULD BE :- 5 %") ; interest = 5
                            print("\n\U0001F600 Your TOTAL INSTALLMENT TIME IS :- 15 Years") ; times = 15
                            print("\n\U0001F600 NOW THE PIN AND VERIFICATION PROCESS IS AHEAD..\n PLEASE CLEAR THEM AND THEN YOUR LOAN WLL BE APPROVED..")
                            time.sleep(1)
                            capout=captcha()
                            if capout==True :
                                lcg5=int(input("\n\U0001F600 DEAR SIR/MADAM,PLEASE ENTER YOUR ACCOUNT PIN CODE.."))
                                lcinget1="select cpin from AA2 where caccno=%s;"
                                lcinget2=(lcg2,)
                                mycursor.execute(lcinget1,lcinget2)
                                mylcdat=mycursor.fetchone()
                                for xlc in mylcdat :
                                    if xlc == lcg5 :
                                        print("\n\U0001F600 ADDING THE MONEY TO YOUR BANK ACCOUNT...")
                                        time.sleep(1)
                                        lccom1="update AA2 set cbalance=cbalance+%s where caccno=%s"
                                        lccom2=(lcg4,lcg2)
                                        mycursor.execute(lccom1,lccom2)
                                        print("\n\U0001F600 CONGRATULATIONS,LOAN AMOUNT SUCCESSFULL ADDED TO YOUR ACCOUNT BALANCE:--)")
                                        print("\n\U0001F600 ENJOY..")
                                        xfans = True
                                        
                                    else :
                                        print("\n\U0001F605 SOMETHING WENT WRONG..")
                                        xfans = False
                                    
                            
                            else :
                                print("\n\U0001F605 SOMETHING WENT WRONG...") #AUTO LOANS ENDED
                                xfans = False
                        #mydbase.commit()
                        #lcalcs(lcg4,interest,times,lcg2)
                        
                    elif lcg3==5 :              #SMALL BUSINESS STARTED
                        ltype="SMALL BUSINESS LOAN"
                        print("\n\U0001F600 YOU HAVE SELECTED SMALL BUSINESS LOANS")
                        print("\n\U0001F600 HERE's SOME INFO ABOUT IT:-")
                        smbl()
                        ltype="SMALL BUSINESS LOAN"
                        lcg4=int(input("\n\U0001F600 DEAR SIR/MADAM,How MUCH LOAN DO YOU WANT :-"))
                        l1=100000
                        l10=1000000
                        c1=10000000
                        c50=500000000
                        if lcg4 < l1 :
                            print("\n\U0001F605 Please ENTER VALID AMOUNT OF MONEY AS MENTIONED:-")
                        elif lcg4 >= l1 and lcg4 <= l10 :
                            print("\n\U0001F600 You ARE PROCEEDING WITH THE LOAN OF :-",lcg4)
                            print("\n\U0001F600 our TOTAL INTEREST WOULD BE :- 2 %") ; interest=2
                            print("\n\U0001F600 Your TOTAL INSTALLMENT TIME IS :- 4 Years") ; times = 4
                            print("\n\U0001F600 NOW THE PIN AND VERIFICATION PROCESS IS AHEAD..\n PLEASE CLEAR THEM AND THEN YOUR LOAN WLL BE APPROVED..")
                            time.sleep(1)
                            capout=captcha()
                            if capout==True :
                                lcg5=int(input("\U0001F600 DEAR SIR/MADAM,PLEASE ENTER YOUR ACCOUNT PIN CODE.."))
                                lcinget1="select cpin from AA2 where caccno=%s;"
                                lcinget2=(lcg2,)
                                mycursor.execute(lcinget1,lcinget2)
                                mylcdat=mycursor.fetchone()
                                for xlc in mylcdat :
                                    if xlc == lcg5 :
                                        print("\n\U0001F600 ADDING THE MONEY TO YOUR BANK ACCOUNT...")
                                        time.sleep(1)
                                        lccom1="update AA2 set cbalance=cbalance+%s where caccno=%s"
                                        lccom2=(lcg4,lcg2)
                                        mycursor.execute(lccom1,lccom2)
                                        print("\n\U0001F600 CONGRATULATIONS,LOAN AMOUNT SUCCESSFULL ADDED TO YOUR ACCOUNT BALANCE:--)")
                                        print("\nENJOY..")
                                        xfans = True
                                    else :
                                        print("\n\U0001F605 SOMETHING WENT WRONG..")
                                        xfans = False
                            else :
                                print("\n\U0001F605 SOMETHING WENT WRONG...")
                                xfans = False
                        elif lcg4 > l10 and lcg4 < c50 :
                            print("\n\U0001F600 You ARE PROCEEDING WITH THE LOAN OF :-",lcg4)
                            print("\n\U0001F600 Your TOTAL INTEREST WOULD BE :- 3 %") ; interest = 3
                            print("\n\U0001F600 Your TOTAL INSTALLMENT TIME IS :- 6 Years") ; times = 6
                            print("\n\U0001F600 NOW THE PIN AND VERIFICATION PROCESS IS AHEAD..\n PLEASE CLEAR THEM AND THEN YOUR LOAN WLL BE APPROVED..")
                            time.sleep(1)
                            capout=captcha()
                            if capout==True :
                                lcg5=int(input("\n\U0001F600 DEAR SIR/MADAM,PLEASE ENTER YOUR ACCOUNT PIN CODE.."))
                                lcinget1="select cpin from AA2 where caccno=%s;"
                                lcinget2=(lcg2,)
                                mycursor.execute(lcinget1,lcinget2)
                                mylcdat=mycursor.fetchone()
                                for xlc in mylcdat :
                                    if xlc == lcg5 :
                                        print("\n\U0001F600 ADDING THE MONEY TO YOUR BANK ACCOUNT...")
                                        time.sleep(1)
                                        lccom1="update AA2 set cbalance=cbalance+%s where caccno=%s"
                                        lccom2=(lcg4,lcg2)
                                        mycursor.execute(lccom1,lccom2)
                                        print("\n\U0001F600 CONGRATULATIONS,LOAN AMOUNT SUCCESSFULL ADDED TO YOUR ACCOUNT BALANCE:--)")
                                        print("\U0001F600 ENJOY..")
                                        xfans = True
                                    else :
                                        print("\n\U0001F605 SOMETHING WENT WRONG..")
                                        xfans = False
                                    
                            
                            else :
                                print("\n\U0001F605 SOMETHING WENT WRONG...")
                                xfans = False
                    else  :
                        print("PLEASE ENTER A VALIND INT ANSWER")
                        getloan()
                        xfans = False
                    if xfans != True :
                        print("SORRY,SOMETHING WENT WRONG...CAN'T ,YOUR LOAN WASN'T DONE..BECAUSE OF SOME TECHNIAL ISSUE..")
                    else :
                        lcalcs(lcg4, interest, times, lcg1,lcg2,ltype)
                        print(lcg4,interest,lcg2,times,lcg1,ltype)
                else :
                    print("\n\U0001F605 SORRY,PLEASE CHECK YOUR ACCOUNT NUMBER,AND TRY AGAIN")
            else:
                print("\U0001F605 Oops,SEEMS LIKE YOU ALREADY ARE DEBTED WITH SOME OTHER LOAN,PLEASE PAY IT FIRST :-)")
        else :
            print("\n\U0001F605 SORRY,PLEASE CHECK YOUR NAME AND THEN TRY AGAIN :-(")
            



    def lpay() :
        print("\n\U0001F607 WELCOME,FOLLOW THE DIRECTIONS BELOW:-)")
        print("PRESS 1 : TO PAY YOUR LOAN")
        print("PRESS 2 : TO GET INFO ABOUT YOUR LOAN :-")
        lpinp1=int(input("\n\U0001F600 Dear SIR/MADAM,Please ENTER The NUMBER OF YOUR DESIRED CHOICE :-"))
        if lpinp1 == 1 :
            print("\n\U0001F607 HERE YOU CAN PAY YOUR LOAN :-")
            lpinp2=str(input("\n\U0001F600 Dear SIR/MADAM,Please ENTER Your NAME :-"))
            lpout1=csupn(lpinp2)
            if lpout1 == True :
                lpinp3=str(input("\n\U0001F600 Dear SIR/MADAM,Please Enter Your ACCOUNT NUMBER :-"))
                lpout2=csupacc(lpinp3)
                if lpout2==True :
                    captout=captcha()
                    if captout== True :
                        print("\n\U0001F600 CAPTCHA SUCCESSFULLY CLEARED")
                        lpcom1="select ltopay from LA4 where caccno=%s;"
                        lpcom2=(lpinp3,)
                        mycursor.execute(lpcom1,lpcom2)
                        lpdat1=mycursor.fetchone()
                        print("\n\U0001F600 Your TOTAL LOAN AMOUNT TO PAY IS :-",lpdat1,"RUPESS")
                        lpinp4=int(input("\n\U0001F600 Enter How Much Loan You WANT To PAY,SIR/MADAM :-"))
                        if type(lpinp4)== int :
                            lpinp5=int(input("\n\U0001F600 Please ENTER YOUR ACCOUNT's PIN"))
                            if type(lpinp5)== int :
                                lpout3=csuppi(lpinp5)
                                if lpout3==True :
                                    if lpinp4 == lpdat1[0] :
                                        print("YOUR LOAN AMOUNT IS COMPLETELY DEPOSITED")
                                        print("\n Now You CAN GET ANOTHER,IF YOU WOULD LIKE TO :-)")
                                        print("\n\U0001F600 LOAN PAID SUCCESSFULLY \U0001F600")
                                        lpcom3 = "update LA4 set status=%s where caccno=%s;"
                                        lpcom4 = ("PAID", lpinp3)
                                        mycursor.execute(lpcom3, lpcom4)
                                        lpcom5 = "insert into LA4 (paid) values(%s) where caccno = %s;"
                                        lpcom6 = (lpinp4,lpinp3)
                                        mycursor.execute(lpcom5, lpcom6)
                                        mydbase.commit()
                                    else:
                                        print("\n\U0001F600 LOAN PAID SUCCESSFULLY \U0001F600")
                                        lpcom3 = "update LA4 set ltopay=%s where caccno=%s;"
                                        lpcom4 = (int(lpdat1[0])- lpinp4, lpinp3)
                                        mycursor.execute(lpcom3, lpcom4)
                                        lpcom5 = "insert into LA4 (paid) values(%s) where caccno =%s;"
                                        lpcom6 = (lpinp4,lpinp3)
                                        mycursor.execute(lpcom5, lpcom6)
                                        mydbase.commit()

                                    
                                else :
                                    print("\n\U0001F605 Please ENTER A VALID PIN")
                            else :
                                print("\n\U0001F605 PLEASE ENTER A VALID AMOUNT")
                                    
                        else :
                            print("\n\U0001F605 PLEASE ENTER A VALID AMOUNT")
                        
                    else :
                        print("\n\U0001F605 CAPTCHA VERIFICATION FAILED")
                    
                else :
                    print("\n\U0001F605 PLEASE CHECK YOUR ACCOUNT NUMBER AND THEN TRY AGAIN")
                    time.sleep(1)
                    print("\n\U0001F600 STARTING THE PROGRAM AGAIN")
                    lpay() #NEED IMPROVEMENT
                    
            else :
                print("\n\U0001F605 PLEASE ENTER THE NAME CORRECTLY")
        elif lpinp1 == 2 :
            print("\n\U0001F607 FOLLOW THE DIRECTIONS PLEASE :-)")
            lpinfoinp1=str(input("\n\U0001F600 Dear SIR,PLEASE ENTER YOUR NAME :-"))
            lpinfoout1=csupn(lpinfoinp1)
            if lpinfoout1== True :
                lpinfoinp2=str(input("\n\U0001F600 Please ENTER Your ACCOUNT NUMBER :-"))
                lpinfoout2=csupacc(lpinfoinp2)
                if lpinfoout2== True :
                    print("\n\U0001F600 HERE's Your LOAN INFO :-")
                    lpcomm1="select cname,caccno,ltype,loan,interest,ltopay,paid,status from LA4 where caccno=%s;"
                    lpcomm2=(lpinfoinp2,)
                    mycursor.execute(lpcomm1,lpcomm2)
                    lpdatx1=mycursor.fetchall()
                    for i in lpdatx1 :
                        cname=i[0]
                        caccno=i[1]
                        ltype=i[2]
                        loan=i[3]
                        interest=i[4]
                        ltopay=i[5]
                        paid=i[6]
                        Status = i[7]
                    print("\n\U0001F600 Your NAME LINKED WITH BANK ACCOUNT IS :-",cname)
                    print("\n\U0001F600 Your ACCOUNT NUMBER IS :-",caccno)
                    print("\n\U0001F600 Your LOAN TYPE IS :-",ltype)
                    print("\n\U0001F600 YOUR LOAN AMOUNT IS :-",loan)
                    print("\n\U0001F600 YOUR INTEREST OVER LOAN IS :-",interest)
                    print("\n\U0001F600 YOU HAVE TO PAY TOTAL LOAN WITH INTEREST AMOUNT :-",ltopay,"RUPEES")
                    print("\n\U0001F600 You HAVE TOTAL PAID OUT OF YOUR LOAN :-",paid,"Rupees")
                    print("\n\U0001F600 You CURRENT STATUS..OF THIS LOAN IS :-",Status)
                    #LOAN INFO WILL CONTINUE
                else :
                    print("\n\U0001F605 PLEASE Enter A VALID ACCOUNT PIN NUMBER")
                

            else :
                print("\n\U0001F605 ENTER THE CORRECT NAME PLEASE :-")
            
        else :
            print("\n\U0001F605 Please Enter Valid CHOICE NUMBER :-)")
            
        


    def credc() :
        print("\n\U0001F607 Welcome Sir/Madam,Here You Will Apply To Get Your CREDIT CARD")
        print("\n\U0001F607 DEAR SIR/MADAM PLEASE ENTER THE DATA BELOW..AND THEN YOU CAN USE YOUR CREDIT CARD")
        credd1=str(input("\n\U0001F600 Dear SIR/MADAM , PLEASE Enter Your Name:-"))
        credd2=str(input("\n\U0001F600 PLEASE ENTER YOUR ACCOUNT NUMBER:-"))
        credc1="select caccno from AA2 where caccno=%s;"
        credc2=(credd2,)
        mycursor.execute(credc1,credc2)
        credout1=mycursor.fetchall()
        for credx in credout1 :
            if credx[0]== credd2 :
                print("\n\U0001F600 NOW Creating Your CREDIT CARD...")
                print("\n\U0001F600 Please Follow The STEPS AHEAD..")
                time.sleep(1)
                capout=captcha()
                if capout==True :
                    credd3=int(input("\n\U0001F600 Dear SIR/MADAM,Please ENTER Your ACCOUNT PIN NUMBER:-"))
                    credc3="select cpin from AA2 where cpin=%s;"
                    credc4=(credd3,)
                    mycursor.execute(credc3,credc4)
                    credout2=mycursor.fetchall()
                    for credx2 in credout2 :
                        if credx2[0] == credd3 :
                            print("\n\U0001F600 OK..ALL CLEAR..")
                            time.sleep(1)
                            print("\n\U0001F600 GETTING YOUR CREDIT CARD READY")
                            cvc=random.randint(100,999)
                            date1x=date.today() #TO BE INSERTED AS DATE,WHEN THE ACCOUNT WAS CREATED
                            curxmonth1=date1x.month
                            curxyear1=date1x.year
                            expmon=curxmonth1
                            expyear=curxyear1+3
                            expdateformat=str(str(expmon)+"/"+str(expyear))
                            
                            credc5="select cname,cmob,cbalance from AA2 where caccno=%s;"
                            credc6=(credd2,)
                            mycursor.execute(credc5,credc6)
                            credout3=mycursor.fetchall()
                            for credx3 in credout3 :
                                cname=credx3[0]
                                cmob=credx3[1]
                                cbalance=credx3[2]
                            credc7="insert into CA3 (cname,cmob,cpin,creditcno,cvc,expdate,cbalance) values(%s,%s,%s,%s,%s,%s,%s);"
                            credc8=(cname,cmob,credd3,credd2,cvc,expdateformat,cbalance)
                            mycursor.execute(credc7,credc8)
                            print("\n\U0001F600 CONGRATULATIONS,YOUR CREDIT CARD IS READY!","\n","\U0001F600"*4)
                            print("\n\U0001F600 YOUR NAME :-",cname)
                            print("\n\U0001F600 YOUR CREDIT CARD NO. :-",credd2)
                            print("\n\U0001F600 YOUR CVC :-",cvc)
                            print("\n\U0001F600 THE EXPIRY DATE :-",expdateformat)
                            print("\n\U0001F600 BALANCE IN YOUR CREDIT CARD :-",cbalance)
                            time.sleep(0.5)
                            print("\n\U0001F600 ENJOY...")
                            print("\n\U0001F600"*4)
                            
                        
                        
                else :
                    print("\n\U0001F605 CLEARING CAPtCHA FAILED..")

                
                
            else :
                print("\n\U0001F605 Please,Check Your ACCOUNT NUMBER Again:-")
                credc()
        #Credit CARD MAKING SUCCESSFUllY DONE...
        #CREDIT CARD P. ENDED



    def tranhis() :         #Transaction History To Play With..:-)
        print("\n\U0001F600  Welcome Sir/Madam , Here You Can Get Account's Transaction History:-")
        print("\n\U0001F600 Let's Get Started:-")
        print("LOADING....")
        time.sleep(1)
        print("\n")
        tac1=str(input("\n\U0001F600 Dear Sir/Madam,Enter Your Name Here:-")) #Getting Input For Name
        trhout1=csupn(tac1) #Fundtion For Name Verification
        if trhout1==True : # If True Then Proceed  Next
            print()
            tac2=str(input("\n\U0001F600 Dear Sir/Madam , Enter Your Account Number:-")) #Getting Input For Account Number
            trhout2=csupacc(tac2) # Function For Account Number Verification
            if trhout2== True : # true Then Proceed Next
                loc1="select * from AA2 where cname=%s and caccno=%s"
                loc2=(tac1,tac2)
                mycursor.execute(loc1,loc2)
                dacinfox1=mycursor.fetchall()
                if mycursor.rowcount==0 : # IF Not Data Fetched..Then This Below And ELSE...Whatever DOWN BELOW,You CAN SEE IT,RIGHT?
                    print("\n\U0001F605 Sorry!Something Went Wrong")
                    print("\n\U0001F605 Please Check your Account Number:-")
                    print("OR contact The BANK SUPPort:-")
                else :
                    capans4=captcha()
                    if capans4==True : # Successfull,Hurray !!
                        tpinno=int(input("\U0001F600 Please Enter Your Account PIN CODE Here:-")) #Getting Input For Account Pin Number ANd Then ALL OLD STORY,PIN VERIFICATION  ,etc.
                        tac3="select cpin from AA2 where cname=%s and caccno=%s"
                        tac4=(tac1,tac2)
                        mycursor.execute(tac3,tac4)
                        pininfo=mycursor.fetchall()
                        for pincheck in pininfo :
                            if pincheck[0] == tpinno :
                                print("\n")
                                print("\U0001F600 PIN Verified Successfully:-")
                                print()
                                print("How Do You Want To Get YOUR TRANSACTION HISTORY:-")
                                print("1.For The ALL TIME TRANSACTION HISTORY")
                                print("2.For The SPECIFIC MONTH")
                                print("3.For The SPECIFIC YEAR")
                                aloop3=1 #Variable For While Loop
                                while aloop3<=3 : # Loop For Choice,3 Attempts Only,After That ? GAME OVER (HeHEHe)
                                    try : # USING TRY AND EXCEPT,Hehehe
                                        print("\n")
                                        thans1=int(input("\U0001F600 Enter Your Choice:-")) #Input CORREcT TYPE,SIGH,,
                                        break
                                    except ValueError :
                                        if aloop3==1 :
                                            print("\U0001F605 Oops!,Something Went Wrong")
                                            print("2 Attempts Left")
                                        elif aloop3==2 :
                                            print("\U0001F605 Please Type Care Fully,Sir/madam")
                                            print("1 Attempts Left")
                                        elif  aloop3==3 :
                                            print("\U0001F605 Please Type Carefully This Time,Sir/Madam")
                                            print("\U0001F605 No Attempts Left")
                                            print("\U0001F605 Starting The Program AGain...")
                                            time.sleep(1)
                                            aloop3+=1
                                        
                                else : #ELSE FOR WHILE Loop
                                    print("\U0001F605 SORRY,No MORE Attempts LEft")
                                    print("\n")
                                if thans1==1 : #Transaction History Of ALL Time
                                    print("\U0001F600 YOUR TRANSACTION HISTORY OF ALL TIME") #WITHDRAWL OF ALL TIME
                                    print("...")
                                    time.sleep(1)
                                    print("\U0001F600 YOUR WITHDRAWL HISTORY")
                                    print("\n")
                                    tcom1="select * from RTA5 where caccno=%s;" # RTA5 :- WITHDRAWL AND TTA5 FOR DEPOSIT
                                    tcom2=(tac2,)
                                    mycursor.execute(tcom1,tcom2)
                                    tdat1=mycursor.fetchall()
                                    if mycursor.rowcount==0 : # IF Nothing ,Then This DOWN BELOW
                                        print("\U0001F605 SORRY,NO AMOUNT WAS WITHDRAWN FROM YOUR ACCOUNT :-")
                                        
                                    else : # OtherWise This..You See It Right ? Me :- Yes SIR
                                        for i in tdat1 :
                                            caccno=i[0]
                                            amountr=i[1]
                                            rdate=i[2]
                                            print(tabulate([["Account Number","AMOUNT","DATE"],[caccno,amountr,rdate]],headers="firstrow",tablefmt="fancy_grid"))


                                    time.sleep(1)
                                    print("\n")
                                    print("\U0001F600 YOUR DEPOSITING HISTORY")  #DEPOSITING FOR WHOLE TIME
                                    tcom1="select * from TTA5 where caccno=%s;" # RTA5 :- WITHDRAWL AND TTA5 FOR DEPOSIT
                                    tcom2=(tac2,)
                                    mycursor.execute(tcom1,tcom2)
                                    tdat1=mycursor.fetchall()
                                    if mycursor.rowcount==0 : #OLD STORY AS ABOVE,MOVE THE BAR OR THE CURSOR,DO SOMETHING ON YOUR OWN Too :-|
                                        print("\U0001F605 SORRY,NO AMOUNT WAS DEPOSITED IN YOUR ACCOUNT :-")
                                        print("\n")
                                    else :
                                        for i in tdat1 :
                                            caccno=i[0]
                                            amountr=i[1]
                                            rdate=i[2]
                                            print(tabulate([["Account Number","AMOUNT","DATE"],[caccno,amountr,rdate]],headers="firstrow",tablefmt="fancy_grid"))
                                    time.sleep(0.4)
                                    print("\n")
                                    print("THIS IS IT... \U0001F600")
                                    
                                elif thans1==2 : #Transaction History Of A SPECIFIC MONTH
                                    ans=str(input("\U0001F600 Which Month Of Transaction History Do You Want:-"))
                                    try :
                                        if int(ans) > 12 : #Month Checking...Or We Can Say Input Checking.You Know We Don't Have More Than 12 Months.. HeHeHe
                                            print("\n")
                                            print("\U0001F605 Please Enter A Valid Month Number")
                                    except SyntaxError : # As My Input Is String , So This :-) For Eg. If I Entered "06" Then I Have To Cut The Zero,Then This All Stuff..
                                        y=ans.split("0")
                                        if y[1] > 12 :
                                            print("\n")
                                            print("\U0001F605 Please Enter A Valid Month Number")
                

                                    if len(ans) == 1 :
                                        ans="0"+ans
                                    tcom1="select rdate from RTA5 where caccno=%s;" # Getting The Dates From Database
                                    tcom2=(tac2,)
                                    mycursor.execute(tcom1,tcom2)
                                    tdat1=mycursor.fetchall()
                                    if mycursor.rowcount == 0 : # If Nothing Found,Then This :__-__-___
                                        print("\n")
                                        print("\U0001F605 SORRY,NO AMOUNT WAS WITHDRAWN FROM YOUR ACCOUNT :-")
                                    elif mycursor.rowcount > 0 : # Elif For ROBUST PROGRAMMING..
                                        bans=True # Variable For Negative Things..OOPS Sorry,I Shouldn't SAy IT (HeHeHe)
                                        for i in tdat1 :
                                            for x in i :
                                                spl=str(x).split("-")
                                                if ans==spl[2] :
                                                    bans=True
                                                    break
                                                else :
                                                    bans=False
                                        if bans== True : #Now The VAriable Is POSITIVE..
                                            thcom1="select caccno,amountr from RTA5 where rdate=%s;"
                                            thcom2=(i[0],)
                                            mycursor.execute(thcom1,thcom2)
                                            thdat1=mycursor.fetchall()
                                            if mycursor.rowcount==0 :
                                                print("\n")
                                                print("\U0001F605 SORRY,NO AMOUNT WAS WITHDRAWN FROM YOUR ACCOUNT :-")
                                            else :
                                                for x in thdat1 :
                                                    caccno=x[0]
                                                    amountr=x[1]
                                                    rdate=i[0]
                                                    print(tabulate([["Account Number","AMOUNT","DATE"],[caccno,amountr,rdate]],headers="firstrow",tablefmt="fancy_grid"))
                                        elif bans==False:
                                            print("\n")
                                            print("\U0001F605 SORRY,NO AMOUNT WAS WITHDRAWN FROM YOUR ACCOUNT :-")

                                            
                                    # DEPOSITING HISTORY OF A SPECIFIC MONTH
                                    tcom1="select tdate from TTA5 where caccno=%s;" # ANother Table,Same Story (Understand It By Yourself)
                                    tcom2=(tac2,)
                                    mycursor.execute(tcom1,tcom2)
                                    tdat1=mycursor.fetchall()
                                    if mycursor.rowcount == 0 :
                                        print("\n")
                                        print("\U0001F605 SORRY,NO AMOUNT WAS WITHDRAWN FROM YOUR ACCOUNT :-")
                                    elif mycursor.rowcount > 0 :
                                        bans=True
                                        for i in tdat1 :
                                            for x in i :
                                                spl=str(x).split("-")
                                                if ans==spl[2] :
                                                    bans=True
                                                    break
                                                else :
                                                    bans=False
                                        if bans== True :
                                            thcom1="select caccno,amountr from TTA5 where tdate=%s;"
                                            thcom2=(i[0],)
                                            mycursor.execute(thcom1,thcom2)
                                            thdat1=mycursor.fetchall()
                                            if mycursor.rowcount==0 :
                                                print("\n")
                                                print("\U0001F605 SORRY,NO AMOUNT WAS WITHDRAWN FROM YOUR ACCOUNT :-")
                                            else :
                                                for x in thdat1 :
                                                    caccno=x[0]
                                                    amountr=x[1]
                                                    rdate=i[0]
                                                    print(tabulate([["Account Number","AMOUNT","DATE"],[caccno,amountr,rdate]],headers="firstrow",tablefmt="fancy_grid"))
                                    
                                elif thans1==3 : #TRANSACTION HISTORY OF A SPECIFIC YEAR
                                    print("\n")
                                    print("\U0001F600 YOUR TRANSACTION HISTORY OF A SPECIFIC YEAR")
                                    print("\n")
                                    ans=str(input("\U0001F600 Enter Which YEAR TRANSACTION HISTORY List Do You Want :-")) #Getting The Input
                                    if len(ans)> 4: # checking The Year If Its Valid Or Not..
                                        print("\U0001F605 SORRY,PLEASE ENTER A VALID YEAR..")
                                        quit
                
                                    elif len(ans)==4 : # Also There IS ELIF TO SOLVE SOME PROBLEMS..
                                        tcom1="select rdate from RTA5 where caccno=%s;" # Getting The Dates Form Database
                                        tcom2=(tac2,)
                                        mycursor.execute(tcom1,tcom2)
                                        tdat1=mycursor.fetchall()
                                        if mycursor.rowcount == 0 :
                                            print("\U0001F605 SORRY,NO AMOUNT WAS WITHDRAWN FROM YOUR ACCOUNT :-")
                                            quit
            
                                        else : # Extracting The Year From The Date And MAtching It
                                            bans=True # Oh,It's The Same OLD STory..(HeHeHE)
                                            for i in tdat1 :
                                                for x in i :
                                                    spl=str(x).split("-")
                                                    if ans==spl[0] :
                                                        bans=True
                                                        break
                                                    else :
                                                        bans=False
                                        if bans== True :
                                            thcom1="select caccno,amountr from RTA5 where rdate=%s;"
                                            thcom2=(i[0],)
                                            mycursor.execute(thcom1,thcom2)
                                            thdat1=mycursor.fetchall()
                                            if mycursor.rowcount==0 :
                                                print("\U0001F605 SORRY,NO AMOUNT WAS WITHDRAWN FROM YOUR ACCOUNT :-")
                                            else :
                                                for x in thdat1 :
                                                    caccno=x[0]
                                                    amountr=x[1]
                                                    rdate=i[0]
                                                    print(tabulate([["Account Number","AMOUNT","DATE"],[caccno,amountr,rdate]],headers="firstrow",tablefmt="fancy_grid"))
                                        elif bans==False:
                                            print("\U0001F605 SORRY,NO AMOUNT WAS WITHDRAWN FROM YOUR ACCOUNT :-")

                                            #FOR DEPOSITING

                                        tcom1="select tdate from TTA5 where caccno=%s;" #For Depositing...This Whole COde...Things Are Repeating..Please Understand..For Now CUT AND PASTE IS EASIER THAN CREATING NEW FUNCTIONS...                                        tcom2=(tac2,)
                                        mycursor.execute(tcom1,tcom2)
                                        tdat1=mycursor.fetchall()
                                        if mycursor.rowcount == 0 :
                                            print("\U0001F605 SORRY,NO AMOUNT WAS DEPOSITED IN YOUR ACCOUNT :-")
            
                                        elif mycursor.rowcount > 0 :
                                            
                                            bans=True
                                            for i in tdat1 :
                                                for x in i :
                                                    spl=str(x).split("-")
                                                    if ans==spl[0] :
                                                        bans=True
                                                        break
                                                    else :
                                                        bans=False
                                            if bans== True :
                                                thcom1="select caccno,amountr from TTA5 where tdate=%s;"
                                                thcom2=(i[0],)
                                                mycursor.execute(thcom1,thcom2)
                                                thdat1=mycursor.fetchall()
                                                if mycursor.rowcount==0 :
                                                    print("\U0001F605 SORRY,NO AMOUNT WAS DEPOSITED IN YOUR ACCOUNT :-")
                                                else :
                                                    for x in thdat1 :
                                                        caccno=x[0]
                                                        amountr=x[1]
                                                        rdate=i[0]
                                                        print(tabulate([["Account Number","AMOUNT","DATE"],[caccno,amountr,rdate]],headers="firstrow",tablefmt="fancy_grid"))
                                            elif bans==False:
                                                print("\U0001F605 SORRY,NO AMOUNT WAS DEPOSITED IN YOUR ACCOUNT :-")
                                else :
                                    print("\n")
                                    print("\U0001F605 INVALID CHOICE")
                                    print("\U0001F605 PLEASE TRY AGAIN:-")
                                    
                    else :
                        print("\U0001F605 Sorry The CAPTCHA You ENTERED WAS WRONG:-") # ALL GREAT ELSES ARE HERE,CLAPPPP (HEHEHE)
            else :
                print("\U0001F605 Dear Sir/Madam,Please CHECK YOUR ACCOUNT NUMBER :-")

        
        else :
            print("\n")
            print("\U0001F605 Please Check Your NAME AGAIN :-")
        

    def csupp() : # THIS IS CUSTOMER SUPPORT..
        print("\n\U0001F607 How Can We Help You Sir :-")
        print("\n\U0001F607 Following Are The Topics That We Can Help You With:-")
        print("1.To Change Your Mobile Number:-")
        print("2.To RESET Your ACCOUNT's PIN CODE:-")
        print("3.To Change Your Name:-")
        print("4.To Change Your Address:-")
        print("\n 5.To EXIT :__):_")
        csupin1= int(input("\n\U0001F600 Enter The Number For Your Desired Choice SIR/MADAM:-")) # Input For Customer's Choice
        if csupin1==3 :#Different Choices,Different Stuff Happens
            print("\n\U0001F600 Here We Are To Change Your NAME Linked With Your Account:-")
            print("\n\U0001F607 Please,Enter The Following Details That WIll Be Asked:-) \U0001F600")
            print("\n\U0001F600 Please Be Cautious:-")
            csupin2=str(input("\n\U0001F600 Dear SIR/MADAM,Please ENTER Your CURRENT NAME REGISTERED IN THE BANK:-")) # Getting The User Current Name
            csupoutb1=csupn(csupin2) #Name Verification
            if csupoutb1== True :
                captout=captcha()
                if captout == True :
                    def checkN1() :
                        
                        astr1=str(1234567890) #Contain All The Natural Number As String
                        astr2=string.punctuation        #Conatins All The Strings
                        csupin3=str(input("\n \U0001F600 Dear SIR/MADAM,Please ENTER Your NEW NAME:-"))
                        bcheck1=list(map(lambda char : char in (astr1+astr2),csupin3)) #Checking ALl The elements And mapping it And Converting It Into The List
                        if any(bcheck1) :   #Loop For Entering A Valid Name
                            print("\n\U0001F605 Please Enter A Valid Name:")
                            return checkN1() #If Any Element In bcheck1 present Then Function Called Again
                        else :
                            return csupin3 #The OutPut
                    csupin3=checkN1()
                    #Receiving The Output
                    tempb=False
                    while tempb== False :
                        csupin4=int(input("\n\U0001F600 Dear SIR/MADAM,Please ENTER Your ACCOUNT's PIN :-")) # getting ACCOUNT's PIN
                        csupoutb2=csuppi(csupin4) # Accounr Pin Verification
                        if csupoutb2==True : # If true,Then ALL TRUE
                            tempb=True
                        else :
                            print("\n\U0001F605 PLEASE ENTER A VALID PIN") #ELse THIS>> (HEHEHE)
                            tempb=False
            
                    csupc1="update AA2 set cname=%s where cname=%s;" # UPDATING THE DETAILS
                    csupc2=(csupin3,csupin2)
                    mycursor.execute(csupc1,csupc2)
                    if mycursor.rowcount > 0 :
                        print("\n\U0001F600 Dear SIR/MADAM,Your NAME Has Been Succssfully Updated :-)")
                        mydbase.commit()
                    else :
                        print("\n\U0001F605 SORRY SIR/MADAM,SOMETHING WENT WRONG") #ELSES >> LIFE SAVERS
                else :
                     print("\n\U0001F605 CAPTCHA VERIFICATION FAILED")
                    
        

                
                 

            else :
                print("\n\U0001F605 THAT WAS WRONG,PLEASE CHECK YOUR NAME AND TRY AGAIN :-)")

        elif csupin1==1 :
            print("\n\U0001F607 Here We Are To Change Your MOBILE PHONE NUMBER Linked With Your Account:-")
            print("\n\U0001F607 Please,Enter The Following Details That WIll Be Asked:-) \U0001F600")
            print("\n\U0001F607 Please Be Cautious:-")
            csupin2=str(input("\n\U0001F600 Dear SIR/MADAM,Please ENTER Your NAME:-"))
            csupoutb1=csupn(csupin2) # NAME VERIFICATION
            if csupoutb1== True :  # IF TRUE THEN USUAL ALL ( :-) )

                captout=captcha()
                if captout == True : # IF TRUE,THEN ALL TRUE
                    caach=str(input("\n\U0001F600 Dear SIR/MADAM,Please ENTER Your ACCOUNT NUMBER:-")) # getting ACCOUNT NUMBER
                    caachout=csupacc(caach) # Account Number Verification
                    if caachout== True :
                        def checkN1() :
                            astr1=str(1234567890) #Contain All The Natural Number As String
                            astr2=string.punctuation        #Conatins All The Strings
                            csupin3=str(input("\n\U0001F600 Dear SIR/MADAM,Please ENTER Your NEW PHONE NUMBER:-")) #TO BE FIXED....2 NOV 2020
                            bcheck1=list(map(lambda char : char in (astr1+astr2),csupin3)) #Checking ALl The elements And mapping it And Converting It Into The List
                            if any(bcheck1) :   #Loop For Entering A Valid NUMBER
                                return csupin3
                        #The OutPut
                            
                            else :
                                print("\n\U0001F605 Please Enter A Valid PHONE NUMBER:")
                                return checkN1() #If Any Element In bcheck1 present Then Function Called Again
                             
                        csupin3=checkN1()
                        #Receiving The Output
                        tempb=False
                        while tempb== False :
                            csupin4=int(input("\n\U0001F600 Dear SIR/MADAM,Please ENTER Your ACCOUNT's PIN :-")) # Getting PIN NUMBER
                            csupoutb2=csuppi(csupin4) #PIN VERFICATION
                            if csupoutb2==True :
                                tempb=True
                            else :
                                print("\n\U0001F605 PLEASE ENTER A VALID PIN")
                                tempb=False
                
                        csupc1="update AA2 set cmob=%s where cname=%s;"
                        csupc2=(csupin3,csupin2)
                        mycursor.execute(csupc1,csupc2)
                        if mycursor.rowcount > 0 :
                            print("\n\U0001F600 Dear SIR/MADAM,Your PHONE NUMBER Has Been Succssfully Updated :-)")
                            mydbase.commit()
                        else :
                            print("\n\U0001F605 SORRY SIR/MADAM,SOMETHING WENT WRONG")
            

                    
                else :
                    print("\n\U0001F605 CAPTCHA VERIFICATION FAILED")
            else :
                print("\n\U0001F605 SORRY,PLEASE CHECK YOUR NAME AND TRY AGAIN")

                
        elif csupin1==2 :
            print("\n\U0001F607 Here We Are To Change Your ACCOUNT PIN NUMBER Linked With Your Account:-")
            print("\n\U0001F607 Please,Enter The Following Details That WIll Be Asked:-) \U0001F600")
            print("\n\U0001F607 Please Be Cautious:-")
            csupin2=str(input("\n\U0001F600 Dear SIR/MADAM,Please ENTER Your NAME:-"))
            csupoutb1=csupn(csupin2)
            if csupoutb1== True :

                captout=captcha()
                if captout == True :
                    caach=str(input("\n\U0001F600 Dear SIR/MADAM,Please ENTER Your ACCOUNT NUMBER:-"))
                    caachout=csupacc(caach)
                    if caachout== True :
                        def checkN1() :
                            csupin3=str(input("\n\U0001F600 Dear SIR/MADAM,Please ENTER Your NEW PIN NUMBER:-"))
                            if csupin3 is  int or len(csupin3) == 5 :
                                return csupin3
                        #The OutPut
                            
                            else :
                                print("\n\U0001F605 Please Enter A Valid PIN NUMBER:")
                                return checkN1() #If Any Element In bcheck1 present Then Function Called Again
                             
                        csupin3=checkN1()
                        #Receiving The Output
                        csupmob=str(input("\n\U0001F600 Please Enter Your MOBILE NUMBER LINKED WITH YOUR ACCOUNT :-"))
                        chckpin=csupm(csupmob)
                        if chckpin == True :
                            csupc1="update AA2 set cpin=%s where caccno=%s;"
                            csupc2=(csupin3,caach)
                            mycursor.execute(csupc1,csupc2)
                            if mycursor.rowcount > 0 :
                                print("\n\U0001F600 Dear SIR/MADAM,Your PIN NUMBER Has Been Succssfully Updated :-)")
                                mydbase.commit()
                            else :
                                print("\n\U0001F605 SORRY SIR/MADAM,SOMETHING WENT WRONG")
                        else :
                            print("\n\U0001F605 SORRY,PLEASE ENTER YOUR VALID PHONE NUMBER :-")
                
                        
                else :
                    print("\n\U0001F605 CAPTCHA VERIFICATION FAILED")
            else :
                print("\n\U0001F605 SORRY,PLEASE CHECK YOUR NAME AND TRY AGAIN")

                
        elif csupin1==4 :
            print("\n\U0001F607 Here We Are To Change Your ADDRESS Linked With Your Account:-")
            print("\n\U0001F607 Please,Enter The Following Details That WIll Be Asked:-) \U0001F600")
            print("\n\U0001F607 Please Be Cautious:-")
            csupin2=str(input("\n\U0001F600 Dear SIR/MADAM,Please ENTER Your NAME:-"))
            csupoutb1=csupn(csupin2)
            if csupoutb1== True :

                captout=captcha()
                if captout == True :
                    caach=str(input("\n\U0001F600 Dear SIR/MADAM,Please ENTER Your ACCOUNT NUMBER:-"))
                    caachout=csupacc(caach)
                    if caachout== True :
                        csupin3=str(input("\n\U0001F600 Dear SIR/MADAM,Please ENTER Your NEW ADDRESS:-"))
                             
                        tempb=False
                        while tempb== False :
                            csupin4=int(input("\n\U0001F600 Dear SIR/MADAM,Please ENTER Your ACCOUNT's PIN :-"))
                            csupoutb2=csuppi(csupin4)
                            if csupoutb2==True :
                                tempb=True
                            else :
                                print("\n\U0001F605 PLEASE ENTER A VALID PIN")
                                tempb=False
                
                        csupc1="update AA2 set cmob=%s where cname=%s;"
                        csupc2=(csupin3,csupin2)
                        mycursor.execute(csupc1,csupc2)
                        if mycursor.rowcount > 0 :
                            print("\n\U0001F600 Dear SIR/MADAM,Your ADDRESS Has Been Succssfully Updated :-)")
                            mydbase.commit()
                        else :
                            print("\n\U0001F605 SORRY SIR/MADAM,SOMETHING WENT WRONG")
                else :
                    print("\n\U0001F605 CAPTCHA VERIFICATION FAILED")
            else :
                print("\n\U0001F605 SORRY,PLEASE CHECK YOUR NAME AND TRY AGAIN")
        else :
            print("\n\U0001F605 SORRY INVALID CHOICE :-)")
            
            
            
            
            

    def ccdet() :
        print("\n\U0001F60A Here You CAn Check Your Bank Details :-")
        print("\n\U0001F607 Please Enter What Asked..")
        print()
        cc1=str(input("\U0001F600 Dear SIR/MADAM Enter Your Name :-")) #Getting The Name From The User
        chckout1=csupn(cc1) #Function To Check The Name
        if chckout1== True : # If Function returned True Then It Proceeds
            print()
            cc2=str(input("\U0001F600 Enter Your Bank Account Number:-")) # Getting The Account Number From The User
            chckout2=csupacc(cc2) # Function To Check Bank Account Number
            if chckout2 == True : #If True Then It Proceeds
                ccm1="select caccno from AA2 where cname=%s and caccno=%s"
                ccm2=(cc1,cc2)
                mycursor.execute(ccm1,ccm2)
                cinfo1=mycursor.fetchall() #Fetching The Results i.e. Account Number ("This Process Is Not Needed")
                for X in cinfo1 : # For Loop For The Data
                    if X[0] == cc2 : # Matching The Account Number Again
                        cans=captcha()
                        if cans==True : # If Given Output Is True,Then Captcha Verified
                            print("\U0001F600 CAPTCHA SUCCESSFULLY VERIFIED \U0001F600")
                            print()
                            cpin=int(input("\U0001F600 Dear Sir/Madam Please Enter Your PIN CODE:-")) # Getting The Input For Account PIN
                            chckout3=csuppi(cpin) # Function For PIN Verification
                            if chckout3 == True : # If Function Returns True Then Program proceeds
                                ccm3="select * from AA2 where cname=%s "  #Oh No,PIN Verification Again,Sorry..I AM NOT IN THE MOOD TO MAKE ANY CHANGES..JUST LET IT GO...
                                ccm4=(cc1,)
                                mycursor.execute(ccm3,ccm4)
                                cinfo2=mycursor.fetchall()
                                for X2 in cinfo2 :
                                    if X2[4] == cpin : # IF PIN Successfully VERIFIED
                                        ccm5="select * from AA2 Where cname=%s and caccno=%s"
                                        ccm6=(cc1,cc2)
                                        mycursor.execute(ccm5,ccm6)
                                        cinfo3=mycursor.fetchall()
                                        if mycursor.rowcount == 0 :
                                            print("SOMETHING WENT WRONG") # IF THERE WAS SOMETHING WRONG OR DATA WAS NOT PRESENT...
                                        else :
                                            for X3 in cinfo3 : #FOR Loop FOR DATA OUTPUT
                                                print("\U0001F600Dear Sir/Madam..Your Bank Details Are :-")
                                                print()
                                                time.sleep(1)
                                                print("\U0001F600Your Name:-",X3[0])
                                                print()
                                                print("\U0001F600 Your Registered Mobile Number :-",X3[1])
                                                print()
                                                print("\U0001F600 Your Account Type :-",X3[2])
                                                print()
                                                print("\U0001F600 Your Account Number:-",X3[3])
                                                print()
                                                print("\U0001F600 Your Account PIN Number Is :-",X3[4])
                                                print()
                                                print("\U0001F600 Your Account Balance Is :-",X3[5],"Rupees")
                            else :
                                print("\nSORRY,THE PIN YOU ENTERED WAS WRONG..PLEASE CHECK AND TRY AGAIN :-)")
                        else :
                            print("\nOOPS,CAPTCHA VERIFICATION FAILED")
                            
                                
                    else :
                        print("\n")
                        print(("\U0001F605 Something Went Wrong,Contact Customer Support Or Check Your Account Details:-")) #ELSE STATEMENTS AHEAD
                                        
                            
            else :
                print("\n")
                print("\U0001F605 PLEASE,CHECK YOUR ACCOUNT NUMBER AND THEN TRY AGAIN \U0001F600")
            
        else :
            print()
            print("\U0001F605 PLEASE,CHECK YOUR NAME AND THEN TRY AGAIN:-")

    # THIS IS IT..
    #BYE CCDET()
    #HeHEHEHE
        

    def binfo() :
        print("\n\U0001F605 ABOUT OUR BANK:-")
        time.sleep(1)
        print("\U0001F600"*10,"WELCOME TO THE OUR BANK:-","\U0001F600"*10)
        time.sleep(0.5)
        print("   "*10,"BY TANUJ VERMA :-)")
        time.sleep(0.5)
        print("App VERSION :- X.10")
        print("\n STATUS :- WORKING PERFECTLY")
        time.sleep(0.5)
        print("\n Dear Sir/Madam \n")
        print("\n This Is OUR BANK...Trusted By All WORLD PEOPLE")
        print("\nOUR PEOPLE ARE WORKING HARD ALL DAY-NIGHT TO MAKE OUR BANK SECURE AND FAST:-")
        print("\nTHIS  APPLICATION AND THE BANK Is BUILT AND ESTABLISHED BY ..... VERMA.HOPE YOU ARE ALL ENJOYING WELL.I PROMISE THAT THIS BANK WILL BE SECURE..AND TRUST WORTHY.")
        print("\nALL OF THIS WAS NOT POSSIBLE WITHOUT YOU MY FAITHFUL CUSTOMERS.")
        time.sleep(0.5)
        print("\n \n VISIT OURvvzzBANK.com TO KNOW ABOUT TERMS AND CONDITIONS:-")
        time.sleep(0.5)
        print("\n \n PLEASE STAY AT OUR WEBSITE OURvvzzBANK.com FOR LATEST UPDATES AND CHANGES...")
        print(" \n \n ENJOY :- ","\U0001F600"*4)
        time.sleep(0.5)
        print("\n \n GOOD BYE :-","\U0001F600"*5,"....")

except ValueError :
    print("Please,Write Your Answers Valid And Correct...")
    print("Hey..Now Face The Consequences..")
    time.sleep(1)
    print("NOW,AS YOUR PUNISHMENT..STARTING YOUR PROGRAM..HEHEHE")
    OBankM()
    

    
    
                            
                    
                        
                
            
        
        
    
        
        
        
                                
