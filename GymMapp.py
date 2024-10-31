from customtkinter import *
from tkinter import *
import mysql.connector
from calendar import *
from tkinter import messagebox
from datetime import date,timedelta
import datetime
try:
   import pywhatkit
except:
   pass
from PIL import Image
windows=CTk(fg_color="#838B8B")
windows.title("GYM MAPP")
windows.geometry("1190x630+55+10")
windows.resizable(False,False)
#windows.configure(bg="#838B8B")
fordatabase,forblinking,forPhotoDel=0,0,0
#FFFFFFFFFFFFFFFFFFF
def callback(event):
    firstFrame.configure()
firstFrame=CTkFrame(windows,fg_color="white",width=400,height=500)
firstFrame.pack(pady=60)
firstFrame.bind("<Enter>", callback)
#EventEEEEEEEEEEEEEEE
def databaseConectionforappExpiry():
   global fordatabase12,con12,exprdateconvert12 
   fordatabase12=0
   try:
      con12=mysql.connector.connect(host="localhost",port="1073",user="root",
      password="Catbox@@7383",database="userid")
      curs=con12.cursor() 
      curs.execute("select * from pass")
      for row in curs:
               use=row[0]
               pass1=row[1]
               expdate1=row[2]
               year1,year2,year3,year4,m1,m2,d1,d2=int(expdate1[0]),int(expdate1[1]),int(expdate1[2]),int(expdate1[3]),int(expdate1[5]),int(expdate1[6]),int(expdate1[8]),int(expdate1[9])
               d1,m1,year1=int("%d%d" % (d1,d2)),int("%d%d" % (m1,m2)),int("%d%d%d%d" % (year1,year2,year3,year4))
               exprdateconvert12=datetime.date(year1,m1,d1) 
   except:
      fordatabase12=90
def StratLogin(l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11):
   databaseConectionforappExpiry()
   global leb3,userEntry,userFrame,paswordEntry,passwordFrame,forgetBuutton,changeBuutton,CreateBuutton,LoginBuutton
   leb3=CTkLabel(windows,text="Login Here",bg_color="white",fg_color="white",font=("arial",19,"bold"))
   leb3.place(x=540,y=110)
   userEntry=CTkEntry(windows,font=("arial",14),fg_color="white",border_width=0,text_color="black",bg_color="white")
   userEntry.place(x=485,y=200)
   userEntry.insert(0,"Username")
   userEntry.bind("<FocusIn>",lambda event,var1=1:DeletUseAndPas(event,var1))
   userFrame=CTkFrame(windows,width=250,height=3,fg_color="black")
   userFrame.place(x=475,y=223)
   paswordEntry=CTkEntry(windows,font=("arial",14),fg_color="white",text_color="black",border_width=0,bg_color="white")
   paswordEntry.place(x=485,y=300)
   paswordEntry.insert(0,"Password")
   paswordEntry.bind("<FocusIn>",lambda event,var1=2:DeletUseAndPas(event,var1))
   passwordFrame=CTkFrame(windows,width=250,height=3,fg_color="black")
   passwordFrame.place(x=475,y=323)
   forgetBuutton=CTkButton(windows,text="ForgetPassword",bg_color="white",fg_color="white",font=("verdana",13,"underline"),text_color="black"
                        ,cursor="hand2")
   forgetBuutton.place(x=459,y=380)
   changeBuutton=CTkButton(windows,text="ChangePassword",bg_color="white",fg_color="white",font=("verdana",13,"underline"),text_color="black"
                        ,cursor="hand2",)
   changeBuutton.place(x=600,y=380)
   CreateBuutton=CTkButton(windows,text="CreateAccount",bg_color="white",fg_color="white",font=("verdana",13,"underline"),text_color="black"
                        ,cursor="hand2",command=CreateAccount)
   CreateBuutton.place(x=530,y=430)
   LoginBuutton=CTkButton(windows,text="Login",bg_color="white",fg_color="red",font=("arial",30,),text_color="white"
   ,cursor="hand2",width=200,command=LoginButton1)
   LoginBuutton.place(x=495,y=490)
   l1.destroy()
   l2.destroy()
   l3.destroy()
   l4.destroy()
   l5.destroy()
   l6.destroy()
   l7.destroy()
   l8.destroy()
   l9.destroy()
   l10.destroy()
   l11.destroy()
lb1= CTkLabel(windows, text="Please")
ent1=CTkEntry(windows)
bt1=CTkButton(windows, text="Confirm")
back_button =CTkButton(windows, text="Back")
lb2=CTkLabel(windows, text="Please Enter")
lb3=CTkLabel(windows, text="Please go")
lb4=CTkLabel(windows, text="Please Read")
lb5=CTkLabel(windows, text="Please Ride")
lb6=CTkLabel(windows, text="Please Swiming")
lb7=CTkLabel(windows, text="Please Swiming1")
lb8=CTkLabel(windows, text="Please Swiming2")
def DeletUseAndPas(event,get1):
   global forPhotoDel
   forPhotoDel=87
   if(get1==1):
      userEntry.delete(0,END)
      userEntry.configure(font=("verdana",13))
      if(paswordEntry.get()==""):
         paswordEntry.configure(show="",font=("arial",13))
         paswordEntry.insert(0,"Password")
   if(get1==2):
      photo1() 
      paswordEntry.delete(0,END)
      paswordEntry.configure(show="*",font=("verdana",13,))
      if(userEntry.get()==""):
         userEntry.insert(0,"Username")
         userEntry.configure(font=("arial",13))
##Used tkinter module
def hidepass():
   photo.configure(file="StaticContent/eye3.png")
   paswordEntry.configure(show="*")
   x1.configure(command=showpass)
def showpass():
   if(paswordEntry.get()=="Password" or paswordEntry.get()==""):
      pass
   else:
      photo.configure(file="StaticContent/openeye10.png")
      paswordEntry.configure(show="")
      x1.configure(command=hidepass)
def photo1():
   global x1,photo
   photo=PhotoImage(file="StaticContent/eye3.png")
   x1=Button(windows,image=photo,bg="white",bd=0,command=showpass,cursor='hand2',activebackground="white",)
   x1.place(x=1040,y=455)
def databaseConect():
   global fordatabase,con 
   try:
      con=mysql.connector.connect(host="localhost",port="1073",user="root",
      password="Catbox@@7383",database="userid")  
   except:
      fordatabase=90
      dBLable=Label(firstFrame,text="DataBase Connection Failed",font=("arial",12,NORMAL),fg="RED",bg="white")
      dBLable.place(x=95,y=10)
def databaseConectionforappExpiry():
   global fordatabase12,con12,exprdateconvert12 
   fordatabase12=0
   try:
      con12=mysql.connector.connect(host="localhost",port="1073",user="root",
      password="Catbox@@7383",database="userid")
      curs=con12.cursor() 
      curs.execute("select * from pass")
      for row in curs:
               use=row[0]
               pass1=row[1]
               expdate1=row[2]
               year1,year2,year3,year4,m1,m2,d1,d2=int(expdate1[0]),int(expdate1[1]),int(expdate1[2]),int(expdate1[3]),int(expdate1[5]),int(expdate1[6]),int(expdate1[8]),int(expdate1[9])
               d1,m1,year1=int("%d%d" % (d1,d2)),int("%d%d" % (m1,m2)),int("%d%d%d%d" % (year1,year2,year3,year4))
               exprdateconvert12=datetime.date(year1,m1,d1) 
   except:
      fordatabase12=90
def LoginButton1():
   forError,forExpireSubscription=0,0
   databaseConect()
   if(fordatabase==0):
      v1=userEntry.get() 
      v2=paswordEntry.get()
      use=""
      pass1=""
      expdate1=""
      q1="select * from pass"
      curs=con.cursor()
      try:
         curs.execute(q1)
      except:
         forError=91
      if(forError==0):
         if(forError==0):
            for row in curs:
               use=row[0]

               
               pass1=row[1]
               expdate1=row[2]
               year1,year2,year3,year4,m1,m2,d1,d2=int(expdate1[0]),int(expdate1[1]),int(expdate1[2]),int(expdate1[3]),int(expdate1[5]),int(expdate1[6]),int(expdate1[8]),int(expdate1[9])
               d1,m1,year1=int("%d%d" % (d1,d2)),int("%d%d" % (m1,m2)),int("%d%d%d%d" % (year1,year2,year3,year4))
               exprdateconvert=datetime.date(year1,m1,d1)
               currentdate10=date.today()
               print(currentdate10,exprdateconvert)
               if(currentdate10>exprdateconvert):
                 forExpireSubscription=17
         if(forExpireSubscription==17):
           forExpLable=Label(firstFrame,text="Your Subscription Expired,Please Renew",bg="white",fg="red",font=("areal",13,"italic"))
           forExpLable.place(x=45,y=10)
         elif use==v1 and pass1==v2:
           messagebox.showinfo("Successfull","Successfull Loged")
           windows.destroy()
           import HomePage
         elif v1==""or v2=="":
           messagebox.showinfo("All Field Required","Pleass Enter User Id And Password")
         else:
           messagebox.showerror("ERROR","Invalid UserId OR Password")
      else:
         messagebox.showerror("Create Userid",'Firstly,Create UserID and Password')
def DeleteCreateUsername(event): 
    userName.delete(0,END)
    userName.configure(text_color="#2E2E2E")
    if(ConformpaswordEntry.get()==""):
       ConformpaswordEntry.configure(text_color="red")
       ConformpaswordEntry.insert(0,"Enter Conform Password")
    if(CreatepaswordEntry.get()==""):
       CreatepaswordEntry.configure(text_color="red")
       CreatepaswordEntry.insert(0,"Enter Password")
    if(productKey.get()==""):
       productKey.configure(text_color="red",show="",font=("arial",13))
       productKey.insert(0,"Enter Product Key")
def DeleteCreatePassword(event): 
    CreatepaswordEntry.delete(0,END)
    CreatepaswordEntry.configure(text_color="#2E2E2E")
    if(userName.get()==""):
       userName.configure(text_color="red")
       userName.insert(0,"Enter Username")
    if(ConformpaswordEntry.get()==""):
       ConformpaswordEntry.configure(text_color="red")
       ConformpaswordEntry.insert(0,"Enter Conform Password")
    if(productKey.get()==""):
       productKey.configure(text_color="red",show="",font=("arial",13))
       productKey.insert(0,"Enter Product Key")
def DeleteconformPassword(event): 
    ConformpaswordEntry.delete(0,END)
    ConformpaswordEntry.configure(text_color="#2E2E2E")
    if(CreatepaswordEntry.get()==""):
       CreatepaswordEntry.configure(text_color="red")
       CreatepaswordEntry.insert(0,"Enter Password")
    if(userName.get()==""):
       userName.configure(text_color="red")
       userName.insert(0,"Enter Username")
    if(productKey.get()==""):
       productKey.configure(text_color="red",show="",font=("arial",13))
       productKey.insert(0,"Enter Product Key")
def DeleteProductKey(event): 
   productKey.delete(0,END)
   productKey.configure(text_color="#2E2E2E")
   if(userName.get()==""):
      userName.configure(text_color="red")
      userName.insert(0,"Enter Username")
   if(CreatepaswordEntry.get()==""):
       CreatepaswordEntry.configure(text_color="red")
       CreatepaswordEntry.insert(0,"Enter Password")
   if(ConformpaswordEntry.get()==""):
      ConformpaswordEntry.configure(text_color="red")
      ConformpaswordEntry.insert(0,"Enter Conform Password")
   productKey.configure(show="*",font=("verdana",13))
def CreateAccount():
   global userName,usernameFrame,CreatepaswordEntry,CreatepasswordFrame,ConformpaswordEntry,ConformpasswordFrame,SubmitBuutton,BackBuutton,createLable,productKey,productKeyFrame
   createLable=CTkLabel(windows,text="Create Your Account",fg_color="white",text_color="black",font=("arial",17,"bold"))
   createLable.place(x=510,y=100)
   userName=CTkEntry(windows,font=("arial",15),fg_color="white",border_width=0,text_color="black",bg_color="white",width=200)
   userName.place(x=485,y=180)
   userName.insert(0,"Enter Username")
   userName.bind("<FocusIn>",DeleteCreateUsername)
   usernameFrame=CTkFrame(windows,width=250,height=3,fg_color="black")
   usernameFrame.place(x=475,y=203)
   CreatepaswordEntry=CTkEntry(windows,font=("arial",15),fg_color="white",border_width=0,text_color="black",bg_color="white",width=200)
   CreatepaswordEntry.place(x=485,y=257)
   CreatepaswordEntry.insert(0,"Enter Password")
   CreatepaswordEntry.bind("<FocusIn>",DeleteCreatePassword)
   CreatepasswordFrame=CTkFrame(windows,width=250,height=3,fg_color="black")
   CreatepasswordFrame.place(x=475,y=280)
   ConformpaswordEntry=CTkEntry(windows,font=("arial",15),fg_color="white",border_width=0,text_color="black",bg_color="white",width=200)
   ConformpaswordEntry.place(x=485,y=334)
   ConformpaswordEntry.insert(0,"Enter Conform Password")
   ConformpaswordEntry.bind("<FocusIn>",DeleteconformPassword)
   ConformpasswordFrame=CTkFrame(windows,width=250,height=3,fg_color="black")
   ConformpasswordFrame.place(x=475,y=357)
   productKey=CTkEntry(windows,font=("arial",15),fg_color="white",border_width=0,text_color="black",bg_color="white",width=200)
   productKey.place(x=485,y=411)
   productKey.insert(0,"Enter Product Key")
   productKey.bind("<FocusIn>",DeleteProductKey)
   productKeyFrame=CTkFrame(windows,width=250,height=3,fg_color="black")
   productKeyFrame.place(x=475,y=434)
   SubmitBuutton=CTkButton(windows,text="Submit",border_width=0,fg_color="#EE2C2C",text_color="white",font=("arial",30)
                        ,cursor="hand2",width=130,command=UserAccountData,bg_color="white")
   SubmitBuutton.place(x=455,y=480)
   BackBuutton=CTkButton(windows,text="Back",border_width=0,fg_color="#00BFFF",text_color="white",font=("arial",30)
                        ,cursor="hand2",width=130,bg_color="white",
   command=lambda:StratLogin(createLable,userName,usernameFrame,CreatepaswordEntry,CreatepasswordFrame,ConformpaswordEntry,ConformpasswordFrame,SubmitBuutton,BackBuutton,productKey,productKeyFrame))
   BackBuutton.place(x=618,y=480)
   leb3.destroy()
   userEntry.destroy()
   userFrame.destroy()
   paswordEntry.destroy()
   passwordFrame.destroy()
   forgetBuutton.destroy()
   changeBuutton.destroy()
   CreateBuutton.destroy()
   LoginBuutton.destroy()
   if(forPhotoDel==87):
      x1.destroy()
def UserAccountData():
   expiryPlantoday=datetime.datetime.now()+timedelta(days=90)
   expiryPlan=expiryPlantoday.strftime("%Y/%m/%d")
   productKeyvalueforAppprotection="Inheritance@@7383"
   productKeyValue=productKey.get()
   u=userName.get()
   p=CreatepaswordEntry.get()
   c=ConformpaswordEntry.get()
   if(u=="Enter Username" or p=="Enter Password" or c=="Enter Conform Password" or productKeyValue=="Enter Product Key"):
      messagebox.showerror("Error","Please Enter New Data In All Fields")
   elif(p!=c):
      messagebox.showerror("Mismatched","Password And Conform Password must be same")
   elif(len(u)<8 or len(u)>12 or len(p)<8 or len(p)>12):
       messagebox.showerror("Charectoar Limit","UserName And Password must be Minimum 8 And Maximum 12 Element")
   elif(productKeyValue!=productKeyvalueforAppprotection):
      productKeyFrame.config(highlightthickness=2,highlightbackground="red")
   else:
       databaseConect()
       if(fordatabase==0):
          st="create table if not exists pass(userid varchar(12),pass varchar(12),ExpDate varchar(20))"
          cur=con.cursor()
          cur.execute(st) 
          q1="select * from pass"
          cur.execute(q1)
          result1=cur.fetchall()
          if(len(result1)==0):
            str="insert into pass( userid,pass,ExpDate) values(%s,%s,%s)"
            val=(u,p,expiryPlan)
            cur.execute(str,val)
            con.commit()
            messagebox.showinfo("Success","You created Successfully")
          else:
            messagebox.showinfo("Already Exist","You have Already Created")
## Here Tkinter 
StratLogin(lb1,ent1,bt1,back_button,lb2,lb3,lb4,lb5,lb6,lb7,lb8)
def blink_label(label):
    global forblinking
    if (forblinking==0):
        planexpireLabel.configure(text_color="red",fg_color="white")
        forblinking=forblinking+1
    else:
        planexpireLabel.configure(text_color="white")
        forblinking=0
    windows.after(700, lambda: blink_label(label))
    
if(fordatabase12==0):
   global planexpireLabel
   dateCalculating=exprdateconvert12-timedelta(days=5)
   dateCalculating90days=exprdateconvert12+timedelta(days=90)
   if(date.today()>=dateCalculating and date.today()<=exprdateconvert12):
      planexpireLabel=CTkLabel(firstFrame,text="Your subscription is expiring soon",fg_color='white',text_color="red",font=("Helvetica", 17))
      planexpireLabel.place(x=70,y=10)
      blink_label(planexpireLabel)
windows.mainloop()
