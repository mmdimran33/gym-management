import tkcalendar as calk
import mysql.connector
from tkinter import messagebox
from tkinter import ttk
from tkinter import PhotoImage
from datetime import timedelta,date
import datetime
import os,subprocess
from tkinter import *
try:
   import pywhatkit
except:
    pass
from customtkinter import *
from PIL import Image
home=CTk()
home.geometry("1190x620+35+10")
home.resizable(False,False)
home.configure(fg_color='#7A8B8B')
home.title("GYM MAPP")
firstFrame=CTkFrame(home,fg_color="white",width=180,height=615,border_width=3)
firstFrame.place(x=1,y=0)
d,deletLableforSelect=0,0 #""" This globle Varialble Deleting text field Value """
forEntry1,checkValue,checkValue1,Ent,re,fordestroy,fordestroy1,res,secondFrame,fordeletingmsg=0,0,0,0,0,0,0,0,0,0#Deliting success Massege  
def AddEmployee1():
     global forEntry1,forEntry2,DisplayWind1,l_var
     global receiptEntry,nameEntry,phoneEntry,firstPaymentEntry,paymentUnpaid,paymentDateEntry,ageEntry,JoiningEntry,expireEntry,combobox,dateofbearthEntry
     DisplayWind1=CTkToplevel()
     DisplayWind1.geometry("750x593+490+50")
     DisplayWind1.grab_set()
     DisplayWind1.title("Client's Registration")
     DisplayWind1.resizable(False,False)
     DisplayWind1.configure(fg_color="#7A8B8B")
     secondFrame=CTkFrame(DisplayWind1,fg_color="white",width=845,height=553,border_color="red",bg_color="white")
     secondFrame.place(x=0,y=40)
     lb2=CTkLabel(DisplayWind1,text="REGISTRATION OF CLIENT",fg_color="#7A8B8B",text_color="#8B2323",font=("arial",15,"bold"))
     lb2.pack(pady=6)
     receiptEntry=Entry(DisplayWind1,font=("arial",13),bd=0,fg="#2E2E2E",width=27)
     receiptEntry.place(x=390,y=92)
     receiptEntry.insert(0,"Receipt Number")
     receiptEntry.bind("<Button-1>",lambda event,var1=1:DeletUsername(var1))
     reciptFrame=Frame(DisplayWind1,width=386,height=4,bg="black")
     reciptFrame.place(x=370,y=125)
     nameEntry=Entry(DisplayWind1,font=("arial",13),bd=0,fg="#2E2E2E",width=27)
     nameEntry.place(x=390,y=162)
     nameEntry.insert(0,"Client Name")
     nameEntry.bind("<Button-1>",lambda event,var1=2:DeletUsername(var1))
     userFrame=Frame(DisplayWind1,width=386,height=4,bg="black")
     userFrame.place(x=370,y=195)
     phoneEntry=Entry(DisplayWind1,font=("arial",13),bd=0,fg="#2E2E2E",width=27)
     phoneEntry.place(x=390,y=232)
     phoneFrame=Frame(DisplayWind1,width=386,height=4,bg="black")
     phoneFrame.place(x=370,y=265)
     phoneEntry.insert(0,"Phone Number")
     phoneEntry.bind("<Button-1>",lambda event,var1=3:DeletUsername(var1))
     l_var =StringVar()
     combobox=Entry(DisplayWind1, textvariable = l_var,font=("arial",13),bd=0,fg="#2E2E2E",bg="white",state=DISABLED,disabledbackground="white",disabledforeground="#2E2E2E")
     l_var.set("Select-Plan")
     combobox.bind('<Button-1>', lambda e, var = l_var: Click(e, var)) 
     combobox.place(x=390,y=302)
     comboboxFrame=Frame(DisplayWind1,width=386,height=4,bg="black")
     comboboxFrame.place(x=370,y=335)
     firstPaymentEntry=Entry(DisplayWind1,font=("arial",13),bd=0,fg="#2E2E2E",width=27)
     firstPaymentEntry.place(x=390,y=372)
     paymentFrame=Frame(DisplayWind1,width=386,height=4,bg="black")
     paymentFrame.place(x=370,y=405)
     firstPaymentEntry.insert(0,"Paid Amount")
     firstPaymentEntry.bind("<Button-1>",lambda event,var1=5:DeletUsername(var1))
     paymentUnpaid=Entry(DisplayWind1,font=("arial",13),bd=0,fg="#2E2E2E",width=27)
     paymentUnpaid.place(x=390,y=442)
     UnpaidFrame=Frame(DisplayWind1,width=386,height=4,bg="black")
     UnpaidFrame.place(x=370,y=475)
     paymentUnpaid.insert(0,"Unpaid Amount")
     paymentUnpaid.bind("<Button-1>",lambda event,var1=6:DeletUsername(var1))
     paymentDateEntry=Entry(DisplayWind1,font=("arial",13),bd=0,fg="#2E2E2E",width=27)
     paymentDateEntry.place(x=390,y=512)
     paymentDateFrame=Frame(DisplayWind1,width=386,height=4,bg="black")
     paymentDateFrame.place(x=370,y=545)
     paymentDateEntry.insert(0,"Payment Date")
     paymentDateEntry.bind("<Button-1>",lambda event,var1=7:pick_Date1(var1))
    #  ageEntry=Entry(DisplayWind1,font=("arial",13),bd=0,fg="#2E2E2E",width=27)
    #  ageEntry.place(x=390,y=582)
    #  ageFrame=Frame(DisplayWind1,width=386,height=4,bg="black")
    #  ageFrame.place(x=370,y=615)
    #  ageEntry.insert(0,"Client Age")
    #  ageEntry.bind("<Button-1>",lambda event,var1=8:DeletUsername(var1))
     dateofbearthEntry=Entry(DisplayWind1,font=("arial",13),bd=0,fg="#2E2E2E",width=27)
     dateofbearthEntry.place(x=390,y=582)
     dateofbearthEntry.insert(0,"DateOfBirth (YYYY/MM/DD)")
     dateofbearthEntry.bind("<Button-1>",lambda event,var1=50:DeletUsername(var1))
     dateofbearthEntry.bind("<Leave>",CheckingDateOfBearthForamte)
     dateofbearth=Frame(DisplayWind1,width=386,height=4,bg="black")
     dateofbearth.place(x=370,y=615)
     joiningVar=StringVar()
     JoiningEntry=Entry(DisplayWind1,textvariable=joiningVar,font=("arial",13),bd=0,fg="#2E2E2E",width=27,state=DISABLED,disabledbackground="white",disabledforeground="#2E2E2E")
     JoiningEntry.place(x=390,y=652)
     joiningVar.set("Joining Date")
     joinDateFrame=Frame(DisplayWind1,width=386,height=4,bg="black")
     joinDateFrame.place(x=370,y=686)
     JoiningEntry.bind("<Button-1>",lambda event,var1=9:pick_Date1(var1))
     expireEntry=Entry(DisplayWind1,font=("arial",13),bd=0,fg="#2E2E2E",width=27)
     expireEntry.place(x=390,y=722)
     expireEntry.insert(0,"Expiry Date")
     expireEntry.config(state=DISABLED,disabledbackground="white",disabledforeground="#2E2E2E")
     expireFrame=Frame(DisplayWind1,width=386,height=4,bg="black")
     expireFrame.place(x=370,y=755)
     expireEntry.bind("<Button-1>",lambda event,var1=10:pick_Date1(var1))
     submit=CTkButton(DisplayWind1,text="Submit",bg_color="white",fg_color="red",font=("arial",25,),text_color="white"
   ,cursor="hand2",width=140,command=insertingData)
     submit.place(x=305,y=556)
     secondFrame.bind("<Enter>",DeletingsuccessMsg)
def CheckingDateOfBearthForamte(event):
    global dateResult100
    try:
      user_input=dateofbearthEntry.get()
      target_date = datetime.datetime.strptime(user_input,'%Y/%m/%d')
      birthday=target_date.strftime("%Y/%m/%d")
      y1,y2,y3,y4,m1,m2,d1,d2=int(birthday[0]),int(birthday[1]),int(birthday[2]),int(birthday[3]),int(birthday[5]),int(birthday[6]),int(birthday[8]),int(birthday[9])
      d1,m1,y1=int("%d%d" % (d1,d2)),int("%d%d" % (m1,m2)),int("%d%d%d%d" % (y1,y2,y3,y4))
      birth_date = datetime.datetime(y1,m1,d1)
      today1=date.today()
      dateResult100=str(today1.year-birth_date.year)+"Year"
    except ValueError:
       if(user_input!="DateOfBirth (YYYY/MM/DD)" and user_input!=""):
        dateofbearthEntry.delete(0,END)
        messagebox.showerror("ERROR","Invalid Date Formate")
def DeletingsuccessMsg(event10):
     if(fordeletingmsg==69):
        msgLable.destroy()
def Click(e, var):
     if(deletLableforSelect==79):
        msgLable10.destroy()
     a=4
     DeletUsername(a)
     def E(var):
         var.set("1-Month")
     def VG(var):
         var.set("2-Month")
     def G(var):
         var.set("3-Month")
     def P(var):
         var.set("6-Month")
     def Y(var):
         var.set("9-Month")
     def Z(var):
         var.set("1-YEAR")
     e.widget.focus()
     nclst=[(' 1-Month', lambda var = var: E(var)),
             (' 2-Month', lambda var = var: VG(var)),
             (' 3-Month', lambda var = var: G(var)),
             (' 6-Month', lambda var = var: P(var)),
             (' 9-Month', lambda var = var: Y(var)),
             (' 1-YEAR', lambda var = var: Z(var))]
     my_menu =Menu(None, tearoff=0, takefocus=0)
     for (txt, cmd) in nclst:
             my_menu.add_command(label=txt, command=cmd)
             my_menu.add_separator()
     my_menu.tk_popup(e.x_root+40, e.y_root+10,entry="0")
def SelectPlan(e, var):
    def E(var):
        var.set("1-Month")
    def VG(var):
        var.set("2-Month")
    def G(var):
        var.set("3-Month")
    def P(var):
        var.set("6-Month")
    def Y(var):
        var.set("9-Month")
    def Z(var):
        var.set("1-YEAR")
    e.widget.focus()
    nclst=[(' 1-Month', lambda var = var: E(var)),
            (' 2-Month', lambda var = var: VG(var)),
            (' 3-Month', lambda var = var: G(var)),
            (' 6-Month', lambda var = var: P(var)),
            (' 9-Month', lambda var = var: Y(var)),
            (' 1-YEAR', lambda var = var: Z(var))]
    my_menu2=Menu(None, tearoff=0, takefocus=0)
    for (txt, cmd) in nclst:
            my_menu2.add_command(label=txt, command=cmd)
            my_menu2.add_separator()
    my_menu2.tk_popup(e.x_root+40, e.y_root+10,entry="0")
def DeletUsername(getvar): 
    if(getvar==1):
       receiptEntry.delete(0,END)
       Ent=Label(DisplayWind1,text=("Receipt Number"),bg="white",font=("arial",13),fg="red")
       Ent.place(x=388,y=60)
    if(getvar==2):
       nameEntry.delete(0,END)
       NameEnt=Label(DisplayWind1,text=("Client Name"),bg="white",font=("arial",13),fg="red")
       NameEnt.place(x=388,y=132)
    if(getvar==3):
       phoneEntry.delete(0,END)
       phoneEnt=Label(DisplayWind1,text=("Phone Number"),bg="white",font=("arial",13),fg="red")
       phoneEnt.place(x=388,y=202)
    if(getvar==4):
        combobox.config(state=NORMAL)
        combobox.delete(0,END)
        comboboxEnt=Label(DisplayWind1,text=("Select-Plan"),bg="white",font=("arial",13),fg="red")
        comboboxEnt.place(x=388,y=272)
        combobox.config(state=DISABLED)
    if(getvar==5):
       firstPaymentEntry.delete(0,END)
       firstPaymentEnt=Label(DisplayWind1,text=("Paid Amount"),bg="white",font=("arial",13),fg="red")
       firstPaymentEnt.place(x=388,y=342)
    if(getvar==6):
       paymentUnpaid.delete(0,END)
       paymentUnpaidEnt=Label(DisplayWind1,text=("Unpaid Amount"),bg="white",font=("arial",13),fg="red")
       paymentUnpaidEnt.place(x=388,y=412)
    if(getvar==7):
       paymentDateEntry.delete(0,END)
       paymentDateEnt=Label(DisplayWind1,text=("Payment Date"),bg="white",font=("arial",13),fg="red")
       paymentDateEnt.place(x=388,y=482)
       paymentDateEntry.config(state=DISABLED,disabledbackground="white",disabledforeground="#2E2E2E")
    if(getvar==8):
       ageEntry.delete(0,END)
       ageEnt=Label(DisplayWind1,text=("Client Age"),bg="white",font=("arial",13),fg="red")
       ageEnt.place(x=388,y=552)
    if(getvar==9):
       JoiningEntry.configure(state=NORMAL)
       JoiningEntry.delete(0,END)
       JoiningEnt=Label(DisplayWind1,text=("Joining Date"),bg="white",font=("arial",13),fg="red")
       JoiningEnt.place(x=388,y=622)
       JoiningEntry.configure(state=DISABLED)
    if(getvar==10):
       expireEntry.delete(0,END)
    if(getvar==11):
        JoiningEntry.delete(0,END)
        JoiningEntry.insert(0,cal.get_date())
        Datewind1.destroy()
    if(getvar==12):
        expireEntry.delete(0,END)
        expireEntry.insert(0,cal.get_date())
        Datewind1.destroy()
    if(getvar==50):
        dateofbearthEntry.delete(0,END)
        dateofbearthEntryLable=Label(DisplayWind1,text=("DateOfBirth (YYYY/MM/DD)"),bg="white",font=("arial",13),fg="red")
        dateofbearthEntryLable.place(x=388,y=552)
def submitForDatePick(var):
    if(var==7):
        paymentDateEntry.config(state=NORMAL,disabledbackground="white",disabledforeground="#2E2E2E")
        paymentDateEntry.delete(0,END)
        paymentDateEntry.insert(0,cal.get_date())
        paymentDateEntry.config(state=DISABLED,disabledbackground="white",disabledforeground="#2E2E2E")
    if(var==9):
        JoiningEntry.config(state=NORMAL)
        date1=cal.get_date()
        JoiningEntry.insert(0,date1)
        JoiningEntry.config(state=DISABLED)
        d1,d2,m1,m2,y1,y2,y3,y4=int(date1[0]),int(date1[1]),int(date1[3]),int(date1[4]),int(date1[6]),int(date1[7]),int(date1[8]),int(date1[9])
        d1,m1,y1=int("%d%d" % (d1,d2)),int("%d%d" % (m1,m2)),int("%d%d%d%d" % (y1,y2,y3,y4))
        convertinInDate=datetime.datetime(y1,m1,d1)
        if(combobox.get()=="Select-Plan" or combobox.get()==""):
            global deletLableforSelect,msgLable10
            deletLableforSelect=79
            msgLable10=Label(DisplayWind1,text=("Please Select Plan..!"),bg="white",font=("arial",11),fg="red")
            msgLable10.place(x=610,y=280)
        else:
            forstoringresultvalue=""
            if(combobox.get()=="1-Month"):
                store1=convertinInDate+timedelta(days=29)
                forstoringresultvalue=store1.strftime("%d/%m/%Y")
            elif(combobox.get()=="2-Month"):
                store2=convertinInDate+timedelta(days=59)
                forstoringresultvalue=store2.strftime("%d/%m/%Y")
            elif(combobox.get()=="3-Month"):
                store3=convertinInDate+timedelta(days=89)
                forstoringresultvalue=store3.strftime("%d/%m/%Y")
            elif(combobox.get()=="6-Month"):
                store4=convertinInDate+timedelta(days=179)
                forstoringresultvalue=store4.strftime("%d/%m/%Y")
            elif(combobox.get()=="9-Month"):
                store5=convertinInDate+timedelta(days=269)
                forstoringresultvalue=store5.strftime("%d/%m/%Y")
            elif(combobox.get()=="1-YEAR"):
                store6=convertinInDate+timedelta(days=359)
                forstoringresultvalue=store6.strftime("%d/%m/%Y")
            expireEntry.config(state=NORMAL)
            expireEntry.delete(0,END)
            expaireDateEnt=Label(DisplayWind1,text=("Expiry Date"),bg="white",font=("arial",13),fg="red")
            expaireDateEnt.place(x=390,y=694)
            expireEntry.insert(0,forstoringresultvalue)
            expireEntry.config(state=DISABLED)
    Datewind1.destroy()
    if(var==10):
        expireEntry.insert(0,cal.get_date())
    Datewind1.destroy()
    if(var==20):
        paymentDateEntry.configure(state=NORMAL)
        paymentDateEntry.delete(0,END)
        paymentDateEntry.insert(0,cal.get_date())
        paymentDateEntry.configure(state="readonly")
    if(var==21):
        JoiningEntry.configure(state=NORMAL)
        date1=cal.get_date()
        JoiningEntry.delete(0,END)
        JoiningEntry.insert(0,date1)
        JoiningEntry.configure(state="readonly")
        d1,d2,m1,m2,y1,y2,y3,y4=int(date1[0]),int(date1[1]),int(date1[3]),int(date1[4]),int(date1[6]),int(date1[7]),int(date1[8]),int(date1[9])
        d1,m1,y1=int("%d%d" % (d1,d2)),int("%d%d" % (m1,m2)),int("%d%d%d%d" % (y1,y2,y3,y4))
        convertinInDate=datetime.datetime(y1,m1,d1)
        forstoringresultvalue=""
        if(seletcplanCombobox.get()=="1-Month"):
                store1=convertinInDate+timedelta(days=29)
                forstoringresultvalue=store1.strftime("%d/%m/%Y")
        elif(seletcplanCombobox.get()=="2-Month"):
                store2=convertinInDate+timedelta(days=59)
                forstoringresultvalue=store2.strftime("%d/%m/%Y")
        elif(seletcplanCombobox.get()=="3-Month"):
                store3=convertinInDate+timedelta(days=89)
                forstoringresultvalue=store3.strftime("%d/%m/%Y")
        elif(seletcplanCombobox.get()=="6-Month"):
                store4=convertinInDate+timedelta(days=179)
                forstoringresultvalue=store4.strftime("%d/%m/%Y")
        elif(seletcplanCombobox.get()=="9-Month"):
                store5=convertinInDate+timedelta(days=269)
                forstoringresultvalue=store5.strftime("%d/%m/%Y")
        elif(seletcplanCombobox.get()=="1-YEAR"):
                store6=convertinInDate+timedelta(days=359)
                forstoringresultvalue=store6.strftime("%d/%m/%Y")
        expireEntry.configure(state=NORMAL)
        expireEntry.delete(0,END)
        expireEntry.insert(0,forstoringresultvalue)
        expireEntry.configure(state=DISABLED)
def pick_Date1(var):
     DeletUsername(var)
     global Datewind1
     global cal
     global submit_btn
     Datewind1=Toplevel()
     Datewind1.geometry("340x310+310+385")
     Datewind1.grab_set()
     Datewind1.title("Select Date")
     Datewind1.resizable(False,False)
     cal=calk.Calendar(Datewind1,selectmode="day",date_pattern="dd/mm/yyyy")
     cal.place(x=0,y=0)
     submit_btn=Button(Datewind1,text="Submit",command=lambda:submitForDatePick(var),bg="#00BFFF",width=11)
     submit_btn.place(x=105,y=253)
def insertingData():
    a,forPaidamount=0,firstPaymentEntry.get()
    global reciptNo,clientName,phoneNumber,firstPayment,unpaidAmount,payMentDate1,clientAge,joinDate,expaireDate,combobox1,bearthdate
    combobox1=combobox.get()
    reciptNo=receiptEntry.get()
    clientName=nameEntry.get()
    phoneNumber=phoneEntry.get()
    unpaidAmount=paymentUnpaid.get()
    bearthdate=dateofbearthEntry.get()
    try:
       firstPayment=int(firstPaymentEntry.get())
    except ValueError:
        a=10
    payMentDate1=paymentDateEntry.get()
    clientAge=dateResult100
    joinDate=JoiningEntry.get()
    expaireDate=expireEntry.get()
    if(reciptNo=="Receipt Number" or clientName=="Client Name" or phoneNumber=="Phone Number" or unpaidAmount=="Unpaid Amount" or payMentDate1=="Payment Date" or clientAge=="Client Age" or joinDate=="Joining Date" or expaireDate=="Expire Date" or combobox1=="Select-Plan" or forPaidamount=="Paid Amount" or bearthdate=="" or bearthdate=="DateOfBearth (YYYY/MM/DD)"):
        ErrorValue1=IntVar()
        ErrorValue1="Please Enter New Data In All Fields"
        message(ErrorValue1)
    elif(reciptNo=="" or clientName=="" or phoneNumber=="" or unpaidAmount=="" or payMentDate1=="" or clientAge=="" or joinDate=="" or expaireDate=="" or combobox1=="" or forPaidamount==""):
        ErrorValue1=IntVar()
        ErrorValue1="All Fields Is Required"
        message(ErrorValue1)
    elif(a==10):
        firstPaymentEntry.delete(0,END)
        firstPaymentEntry.config(fg="#2E2E2E")
        firstPaymentEnt=Label(DisplayWind1,text=("Paid Amount"),bg="white",font=("arial",13),fg="red")
        firstPaymentEnt.place(x=225,y=224)
        firstPaymentEntry.insert(0,"Invalid Number  X")
    else:
            global msgLable,fordeletingmsg
            con=mysql.connector.connect(host="localhost",port="1073",user="root",
            password="Catbox@@7383",database="userid")  
            st="""create table if not exists inseringData(userid int not null AUTO_INCREMENT,reciptNo varchar(100),clientName varchar(100),phoneNumber varchar(14),plan varchar(30),
            firstPayment int,UnpaidAmount varchar(50),paymentDate varchar(20),ClientAge varchar(10),joiningDate varchar(20),expDate varchar(20),bearthdate varchar(20),PRIMARY KEY (userid))"""
            insertQ1="""insert into inseringData(reciptNo,clientName,phoneNumber,plan,firstPayment,UnpaidAmount
            ,paymentDate,ClientAge,joiningDate,expDate,bearthdate) 
            values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            dataVariable=(reciptNo,clientName,phoneNumber,combobox1,firstPayment, unpaidAmount,payMentDate1,clientAge,joinDate,expaireDate,bearthdate)
            cur=con.cursor()
            cur.execute(st) 
            cur.execute(insertQ1,dataVariable)
            con.commit()
            if(cur.rowcount==1):
               DisplayWind1.destroy()
               AddEmployee1()
               msgLable=Label(DisplayWind1,text="Record Inserted Successfull",font=("Verdan",13),bg="white",fg="Red")
               msgLable.place(x=15,y=543)
               fordeletingmsg=69
def fetchingData():
    global tree1,DisplayWind
    j=0
    con=mysql.connector.connect(host="localhost",port="1073",user="root",password="Catbox@@7383",database="userid")
    cur=con.cursor()
    try:
       a=cur.execute("SELECT userid FROM inseringData")
    except:
        pass
    for row in cur:
        j=j+1
    DisplayWind=CTkToplevel()
    DisplayWind.geometry("1190x620+35+10")
    DisplayWind.grab_set()
    DisplayWind.title("Displaying Client's Data",)
    DisplayWind.resizable(False,False)
    DisplayWind.configure(fg_color="#8B8378")
    SearchLable=CTkLabel(DisplayWind,text=f"Search By Name:",font=("arial",20,"bold"),fg_color="#8B8378",text_color="white")
    SearchLable.place(x=360,y=4)
    SearchEntry=CTkEntry(DisplayWind,width=200,font=("arial",15),border_width=2,text_color='black',)
    SearchEntry.place(x=550,y=3)
    SearchButton=CTkButton(DisplayWind,text="Search",width=110,font=("Arial",15),bg_color="#8B8378",height=28,fg_color="blue",
    text_color="white",command=lambda:SearchMethd(SearchEntry,tree1),hover_color="#228B22")
    SearchButton.place(x=800,y=3)
    TotalClient=Label(DisplayWind,text="Total Number Of Clients:",font=("arial",15,"bold"),bg="#8B8378",fg="white")
    TotalClient.place(x=600,y=870)
    TotalEntry=Entry(DisplayWind,width=10,font=("verdana",10),bd=7,relief=SOLID,bg='#7A8B8B')
    TotalEntry.insert(0,j)
    TotalEntry.place(x=1000,y=870)
    TotalEntry.config(state=DISABLED,disabledbackground="black",disabledforeground="white",justify=CENTER)
    columnVar=("ColumnValue1","ColumnValue2","ColumnValue3","ColumnValue4","ColumnValue5",
               "ColumnValue6", "ColumnValue7","ColumnValue8","ColumnValue9","ColumnValue10","ColumnValue11","ColumnValue12")
    tree1=ttk.Treeview(DisplayWind,columns=columnVar,height=39)
    tree1.place(x=0,y=50)
    #tree1.pack(fill=BOTH,expand=True,padx=10,pady=20)
    tree1.bind('<Button-1>', handle_click)
    tree1.heading(0,text="Userid")
    tree1.heading(1,text="ReciptNo")
    tree1.heading(2,text="ClientName")
    tree1.heading(3,text="PhoneNumber")
    tree1.heading(4,text="Monthly Plan")
    tree1.heading(5,text="PaidAmount") 
    tree1.heading(6,text="UnpaidAmount") 
    tree1.heading(7,text="PaymentDate") 
    tree1.heading(8,text="Age") 
    tree1.heading(9,text="JoiningDate")
    tree1.heading(10,text="ExpiryDate") 
    tree1.heading(11,text="DateOfBirth") 
    tree1['show']='headings'
    styl1=ttk.Style(DisplayWind)
    styl1.theme_names()
    styl1.theme_use('clam')
    styl1.configure(".",font=("arial",10))
    styl1.configure("Treeview.Heading", font=(None, 10),)
    styl1.configure("Custom.TreeView",rowheight=70)
    tree1.column("ColumnValue1",width=70,minwidth=55,stretch=False)
    tree1.column("ColumnValue2",width=120,minwidth=80)
    tree1.column("ColumnValue3",width=265,minwidth=250)
    tree1.column("ColumnValue4",width=165,minwidth=110)
    tree1.column("ColumnValue5",width=135,minwidth=110)
    tree1.column("ColumnValue6",width=120,minwidth=110)
    tree1.column("ColumnValue7",width=140,minwidth=110)
    tree1.column("ColumnValue8",width=140,minwidth=110)
    tree1.column("ColumnValue9",width=100,minwidth=108)
    tree1.column("ColumnValue10",width=175,minwidth=108)
    tree1.column("ColumnValue11",width=175,minwidth=108)
    tree1.column("ColumnValue12",width=175,minwidth=108)
    scrollbar2=ttk.Scrollbar(DisplayWind,orient=VERTICAL)
    scrollbar2.pack(side=RIGHT,fill=Y,pady=50,) 
    tree1.configure(yscrollcommand=scrollbar2.set)
    scrollbar2.config(command=tree1.yview)
    styl1.configure("Vertical.TScrollbar", gripcount=0,background="#242B64", bordercolor="#6C7B8B", 
                    arrowcolor="white",troughcolor="#FFFAFA",darkcolor="#FCE6C9",lightcolor="#FCE6C9",activebackground="black",bd=15)
    try:
       cur.execute("select * from inseringData")
    except:
        pass
    z=0
    for ro in cur:
       tree1.insert('',z,text="",values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5],ro[6],ro[7],ro[8],ro[9],ro[10],ro[11]))
       tree1.bind("<Double-1>",UpdateComponent)
def handle_click(event):
        if tree1.identify_region(event.x, event.y) == "separator":
            return "break"   
def SearchMethd(serachEntr,treeview):
    s1=serachEntr.get()
    con=mysql.connector.connect(host="localhost",port="1073",user="root",
    password="Catbox@@7383",database="userid")  
    cur=con.cursor()
    try:
        cur.execute("select * from inseringData where clientName LIKE '%"+s1+"%'")
        row=cur.fetchall()
        if len(row)>0:
          treeview.delete(*treeview.get_children())  
          for i in row:
              treeview.insert('',END,values=i)
        else:
            treeview.delete(*treeview.get_children())  
    except Exception as e:
        msgLable=Label(DisplayWind,text="No Record Found,Please Add Record",font=("arial",13,NORMAL),fg="Red")
        msgLable.place(x=530,y=300)
def UpdateComponent(event):
    pass
def ClientUpdate():
   updatevalue,forexception10=serEntry.get(),0
   if(updatevalue==""):
      messagebox.showerror("Empty Field","Pleass Enter UserId")
   else:
      global userid1,reciptNo,clientName,phoneNumber,firstPayment,unpaidAmount,payMentDate1,clientAge,joinDate,expaireDate,plan
      con=mysql.connector.connect(host="localhost",port="1073",user="root",
      password="Catbox@@7383",database="userid")  
      cur=con.cursor()
      try:
         cur.execute("select * from inseringdata where userid=%s",(updatevalue,))
         result=cur.fetchall()
      except:
          messagebox.showerror("ERROR","Invalid UserID")
          forexception10=28
      if(forexception10==0):
          if(len(result)==0):
             messagebox.showerror("Error","UserId Not Mached")
          else:
             a=10
             for data in result:
                userid1,reciptNo,clientName,phoneNumber,plan,firstPayment,unpaidAmount,payMentDate1,clientAge,joinDate,expaireDate=data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10]
                GoOnUpdatetextFields()
         #result=cur.fetchall()
def UpdateDetails():
    def changeColor(event):
        serEntry.configure(border_color="green")
    global serEntry,l1,bt2
    l1=CTkLabel(home,text="Enter UserID:",fg_color="#7A8B8B",font=("verdana",15,),text_color='White')
    l1.place(x=360,y=14)
    serEntry=CTkEntry(home,width=220,font=("arial",15),border_width=2,text_color='black',border_color="#007FFF")
    serEntry.place(x=470,y=13)
    serEntry.bind("<Button-1>", changeColor)
    bt2=CTkButton(home,text="Update",width=110,font=("Arial",15),bg_color="#8B8378",height=28,fg_color="blue",
    text_color="white",hover_color="#228B22",command=ClientUpdate)
    bt2.place(x=720,y=14)
def  GoOnUpdatetextFields():
    global useridEntry,receiptEntry,nameEntry,phoneEntry,firstPaymentEntry,paymentUnpaid,paymentDateEntry,ageEntry,JoiningEntry,expireEntry,seletcplanCombobox,DisplayWind2
    serEntry.destroy()
    l1.destroy()
    bt2.destroy()
    DisplayWind2=CTkToplevel()
    DisplayWind2.geometry("700x570+340+50")
    DisplayWind2.grab_set()
    DisplayWind2.title("Displaying Client's Data",)
    DisplayWind2.resizable(False,False)
    DisplayWind2.configure(fg_color="#7A8B8B")
    secondFrame=CTkFrame(DisplayWind2,fg_color="white",width=700,height=570)
    secondFrame.place(x=0,y=40)
    lb1=Label(DisplayWind2,text="Updating Client'S Details",bg="#7A8B8B",fg="blue",font=("arial",15,))
    lb1.pack(pady=6)
    userid=CTkLabel(DisplayWind2,text="User ID:",font=("arial",16),fg_color="white",bg_color="white")
    userid.place(x=70,y=60)
    useridEntry=CTkEntry(DisplayWind2,width=220,font=("arial",15),border_width=1,text_color='black',bg_color="white",border_color="blue",)
    useridEntry.place(x=240,y=60)
    useridEntry.insert(0,userid1)
    useridEntry.configure(state=DISABLED,fg_color="#E0EEEE")
    receipt=CTkLabel(DisplayWind2,text="Receipt Number:",font=("arial",16),fg_color="white",bg_color="white")
    receipt.place(x=70,y=100)
    receiptEntry=CTkEntry(DisplayWind2,width=220,font=("arial",15),border_width=1,text_color='black',bg_color="white",border_color="blue",)
    receiptEntry.place(x=240,y=100)
    receiptEntry.insert(0,reciptNo)
    name=CTkLabel(DisplayWind2,text="Client Name:",font=("arial",16),fg_color="white",bg_color="white")
    name.place(x=70,y=140)
    nameEntry=CTkEntry(DisplayWind2,width=220,font=("arial",15),border_width=1,text_color='black',bg_color="white",border_color="blue",)
    nameEntry.place(x=240,y=140)
    nameEntry.insert(0,clientName)
    phone=CTkLabel(DisplayWind2,text="Phone Number:",font=("arial",16),fg_color="white",bg_color="white")
    phone.place(x=70,y=180)
    phoneEntry=CTkEntry(DisplayWind2,width=220,font=("arial",16),border_width=1,text_color='black',bg_color="white",border_color="blue",)
    phoneEntry.place(x=240,y=180)
    phoneEntry.insert(0,phoneNumber)
    seletcplan=CTkLabel(DisplayWind2,text="Select Plan:",font=("arial",16),fg_color="white",bg_color="white")
    seletcplan.place(x=70,y=220)
    l_var2 =StringVar()
    seletcplanCombobox=CTkEntry(DisplayWind2,textvariable=l_var2,width=220,font=("arial",16),border_width=1,text_color='black',bg_color="white",border_color="blue",)
    seletcplanCombobox.place(x=240,y=220)
    seletcplanCombobox.insert(0,plan)
    seletcplanCombobox.bind('<Button-1>',lambda e, var =l_var2:SelectPlan(e, var)) 
    payment=CTkLabel(DisplayWind2,text="First Payment:",font=("arial",16),fg_color="white",bg_color="white")
    payment.place(x=70,y=260)
    firstPaymentEntry=CTkEntry(DisplayWind2,width=220,font=("arial",16),border_width=1,text_color='black',bg_color="white",border_color="blue",)
    firstPaymentEntry.place(x=240,y=260)
    firstPaymentEntry.insert(0,firstPayment)
    paymentUnpaid=CTkLabel(DisplayWind2,text="Unpaid Amount:",font=("arial",16),fg_color="white",bg_color="white")
    paymentUnpaid.place(x=70,y=300)
    paymentUnpaid=CTkEntry(DisplayWind2,width=220,font=("arial",16),border_width=1,text_color='black',bg_color="white",border_color="blue",)
    paymentUnpaid.place(x=240,y=300)
    paymentUnpaid.insert(0,unpaidAmount)
    paymentDate=CTkLabel(DisplayWind2,text="Payment Date:",font=("arial",16),fg_color="white",bg_color="white")
    paymentDate.place(x=70,y=340)
    paymentDateEntry=CTkEntry(DisplayWind2,width=220,font=("arial",16),border_width=1,text_color='black',bg_color="white",border_color="blue",)
    paymentDateEntry.place(x=240,y=340)
    paymentDateEntry.insert(0,payMentDate1)
    paymentDateEntry.configure(state="readonly")
    paymentDateEntry.bind('<Button-1>' ,lambda event,var1=20:pick_Date1(var1))
    age=CTkLabel(DisplayWind2,text="Client Age:",font=("arial",16),fg_color="white",bg_color="white")
    age.place(x=70,y=380)
    ageEntry=CTkEntry(DisplayWind2,width=220,font=("arial",16),border_width=1,text_color='black',bg_color="white",border_color="blue",)
    ageEntry.place(x=240,y=380)
    ageEntry.insert(0,clientAge)
    Joining=CTkLabel(DisplayWind2,text="Joining Date:",font=("arial",16),fg_color="white",bg_color="white")
    Joining.place(x=70,y=420)
    JoiningEntry=CTkEntry(DisplayWind2,width=220,font=("arial",15),border_width=1,text_color='black',bg_color="white",border_color="blue")
    JoiningEntry.place(x=240,y=420)
    JoiningEntry.insert(0,joinDate)
    JoiningEntry.configure(state="readonly")
    JoiningEntry.bind('<Button>' ,lambda event,var1=21:pick_Date1(var1))
    expire=CTkLabel(DisplayWind2,text="Expiry Date:",font=("arial",16),fg_color="white",bg_color="white")
    expire.place(x=70,y=460)
    expireEntry=CTkEntry(DisplayWind2,width=220,font=("arial",15),border_width=1,text_color='black',bg_color="white",border_color="blue",)
    expireEntry.place(x=240,y=460)
    expireEntry.insert(0,expaireDate)
    expireEntry.configure(state="readonly",fg_color="#E0EEEE")
    update=CTkButton(DisplayWind2,text="Update",bg_color="white",fg_color="red",font=("arial",30,),text_color="white",height=15
   ,cursor="hand2",width=150,command=UpdatingDetails)
    update.place(x=280,y=510)
def UpdatingDetails():
    global d
    selectCombobox,reciptNo,paidAmount=seletcplanCombobox.get(),receiptEntry.get(),firstPaymentEntry.get()
    clientName=nameEntry.get()
    phoneNumber=phoneEntry.get()
    userid=useridEntry.get()
    try:
       firstPayment=int(firstPaymentEntry.get())
    except ValueError:
        d=10
    unpaidAmount=paymentUnpaid.get()
    payMentDate1=paymentDateEntry.get()
    clientAge=ageEntry.get()
    joinDate=JoiningEntry.get()
    expaireDate=expireEntry.get()
    if(reciptNo=="" or selectCombobox=="" or clientName=="" or phoneNumber=="" or unpaidAmount=="" or payMentDate1=="" or clientAge=="" or joinDate=="" or expaireDate=="" or paidAmount==""):
        ErrorValue2=IntVar()
        ErrorValue2="All Fields is required"
        message(ErrorValue2)
    elif(d==10):
       firstPaymentEntry.delete(0,END) 
       firstPaymentEntry.config(fg="red")
       firstPaymentEntry.insert(0,"Invalid Number") 
    else:
      con=mysql.connector.connect(host="localhost",port="1073",user="root",
      password="Catbox@@7383",database="userid")  
      cur=con.cursor()
      q1="update inseringData set reciptNo=%s,clientName=%s,phoneNumber=%s,plan=%s,firstPayment=%s,UnpaidAmount=%s,paymentDate=%s,ClientAge=%s,joiningDate=%s,expDate=%s where userid=%s"
      var=(reciptNo,clientName,phoneNumber,selectCombobox,firstPayment,unpaidAmount,payMentDate1,clientAge,joinDate,expaireDate,userid)
      row=cur.execute(q1,var)
      con.commit()
      if(cur.rowcount==1):
        messagebox.showinfo("Succcess","Records Updated!")
def message(messegeValue):
    msg=CTkToplevel() 
    msg.geometry("250x190+400+360") 
    msg.title("Eroor")
    msg.resizable(False,False)
    msg.grab_set() 
    msg.configure(fg_color="#FFE4C4")
    icon=CTkImage(dark_image=Image.open("StaticContent/ErrorIcon5.png"),size=(50,50))
    imgLable=CTkLabel(msg,image=icon,fg_color="#FFE4C4",text="")
    imgLable.pack(pady=10)
    ValueLable=CTkLabel(msg,text=messegeValue,text_color="red",font=("arial",15),fg_color="#FFE4C4")
    ValueLable.pack(pady=15)
    lineFrame=CTkFrame(msg,width=252,height=3,fg_color="black")
    lineFrame.pack(pady=15)
    OKsubmit=CTkButton(msg,text="OK",border_width=0,fg_color="#EE2C2C",text_color="white",font=("arial",14,)
   ,cursor="hand2",width=70,command=msg.destroy,)
    OKsubmit.place(x=92,y=158)
    msg.mainloop() 
def ExpiredPlan():
    global emptyTable,useridexp,clientNameexp,phoneNumberexp,clientAgeexp,totalexpired
    emptyTable,totalexpired=0,0
    DisplayWind1=CTkToplevel()
    DisplayWind1.geometry("800x570+360+55")
    DisplayWind1.grab_set()
    DisplayWind1.title("Expired Plan")
    DisplayWind1.resizable(False,False)
    DisplayWind1.configure(fg_color="#7A8B8B")
    mainfrm=LabelFrame(DisplayWind1,bg="white",bd=0)
    canvas=Canvas(mainfrm)
    canvas.pack(side=LEFT,fill=BOTH,expand=1)
    scroolbar=ttk.Scrollbar(mainfrm,orient="vertical",command=canvas.yview)  
    scroolbar.pack(side = RIGHT, fill = Y)
    canvas.configure(yscrollcommand=scroolbar.set)
    canvas.bind("<Configure>",lambda e:canvas.configure(scrollregion=canvas.bbox("all")))
    seconframe=Frame(canvas)
    seconframe.pack()
    canvas.create_window((0,0),window=seconframe,anchor="nw")
    mainfrm.place(x=10,y=45,width=1180,height=750)
    sfram=Frame(seconframe,width=1149,height=40,bg="#242B64")
    sfram.pack(padx=0,pady=5)
    klable=Label(sfram,text="UserId",fg="white",bg="#242B64",font=('arial', 11,"bold"))
    klable.place(x=0,y=4)
    klable1=Label(sfram,text="ClientName",fg="white",bg="#242B64",font=('arial', 11,"bold"))
    klable1.place(x=80,y=4)
    klable2=Label(sfram,text="PhoneNumber",fg="white",bg="#242B64",font=('arial', 11,"bold"))
    klable2.place(x=400,y=4)
    klable2=Label(sfram,text="ClientAge",fg="white",bg="#242B64",font=('arial', 11,"bold"))
    klable2.place(x=600,y=4)
    klable2=Label(sfram,text="ExpiryDate",fg="white",bg="#242B64",font=('arial', 11,"bold"))
    klable2.place(x=800,y=4)
    klable2=Label(sfram,text="Status",fg="white",bg="#242B64",font=('arial', 11,"bold"))
    klable2.place(x=1000,y=4)
    msgButton1=CTkButton(DisplayWind1,text="SendMessageOnWhatsApp",font=("Verdana",12,"bold"),fg_color="green",text_color="white",command=SendMessageOnWhatsApp)
    msgButton1.place(x=300,y=536)
    cy=0
    def fun10():  
        global cy
        sfram=Frame(seconframe,width=300,height=25,bg="black")
        sfram.pack(pady=5)
        if(cy==0):
            cy=10
            sfram.config(bg="green",)
            klable=Label(sfram,text=f"Userid",fg="white",bg="green")
            klable.place(x=0,y=0)
            klable1=Label(sfram,text=f"Client Name",fg="white",bg="green")
            klable1.place(x=80)
        else:
            klable=Label(sfram,text=f"Adnan",fg="white",bg="black")
            klable.place(x=0,y=0)
            klable1=Label(sfram,text=f"Kalam",fg="white",bg="black")
            klable1.place(x=80)
            print("Value",cy)
    con=mysql.connector.connect(host="localhost",port="1073",user="root",
    password="Catbox@@7383",database="userid")
    cur10=con.cursor()
    try:
       cur10.execute("select userid,clientName,phoneNumber,clientAge,expDate from inseringData")
    except:
        pass
    for getdat1 in cur10:
        emptyTable=10
        useridexp,clientNameexp,phoneNumberexp,clientAgeexp,expDateexp=getdat1[0],getdat1[1],getdat1[2],getdat1[3],getdat1[4]
        d1,d2,m1,m2,y1,y2,y3,y4=int(expDateexp[0]),int(expDateexp[1]),int(expDateexp[3]),int(expDateexp[4]),int(expDateexp[6]),int(expDateexp[7]),int(expDateexp[8]),int(expDateexp[9])
        d1,m1,y1=int("%d%d" % (d1,d2)),int("%d%d" % (m1,m2)),int("%d%d%d%d" % (y1,y2,y3,y4))
        exprdate=datetime.date(y1,m1,d1)
        currenDate=date.today()
        if(currenDate>exprdate):
            totalexpired=totalexpired+1
            sfram=Frame(seconframe,width=1149,height=35,bg="#A9A9A9")
            sfram.pack(padx=20,pady=1)
            klable=Label(sfram,text=useridexp,fg="black",bg="#A9A9A9",font=("times now",11))
            klable.place(x=0,y=4)
            klable1=Label(sfram,text=clientNameexp,fg="black",bg="#A9A9A9",font=("times now",11))
            klable1.place(x=80,y=4)
            klable2=Label(sfram,text=phoneNumberexp,fg="black",bg="#A9A9A9",font=("times now",11))
            klable2.place(x=400,y=4)
            klable2=Label(sfram,text=clientAgeexp,fg="black",bg="#A9A9A9",font=("times now",11))
            klable2.place(x=602,y=4)
            klable2=Label(sfram,text=expDateexp,fg="black",bg="#A9A9A9",font=("times now",11))
            klable2.place(x=800,y=4)
            klable2=Label(sfram,text="Expired",fg="red",bg="#A9A9A9",font=("times now",11))
            klable2.place(x=1000,y=4)
    if(emptyTable==0):
        ValueLable=Label(DisplayWind1,text="No Registered Record Found",fg="#FFFF00",font=("verdana",13,"bold"),bg="#7A8B8B")
        ValueLable.place(x=295,y=3)
    else:
        ValueLable=Label(DisplayWind1,text=f"Total Expired Plan: {totalexpired}",fg="#FFFF00",font=("verdana",13,"bold"),bg="#7A8B8B")
        ValueLable.place(x=420,y=1)
    DisplayWind1.mainloop()
def hoverButton(eventj1):
    pass
def BackupFun():
    pass1="Catbox@@7383"
    location="Z:\Project/backup1.sql"
    gf=subprocess.call(f"mysqldump -u root -p%s -P 1073 userid>{location}" % pass1,shell=True)
    if(gf==0):
        messagebox.showinfo("Data Backup","Data Backup SuccessFull")
    else:
        messagebox.showerror("Data Backup Error","Please Insert Pendrive,DataBackup Location Not Found")
def SendMessageOnWhatsApp():
    con=mysql.connector.connect(host="localhost",port="1073",user="root",
    password="Catbox@@7383",database="userid")
    cur10=con.cursor()
    try:
       cur10.execute("select expDate, phoneNumber,clientName from inseringData")
       for i in cur10:
           expireValue,phone,nameofclint=i[0],i[1],i[2]
           d1,d2,m1,m2,y1,y2,y3,y4=int(expireValue[0]),int(expireValue[1]),int(expireValue[3]),int(expireValue[4]),int(expireValue[6]),int(expireValue[7]),int(expireValue[8]),int(expireValue[9])
           d1,m1,y1=int("%d%d" % (d1,d2)),int("%d%d" % (m1,m2)),int("%d%d%d%d" % (y1,y2,y3,y4))
           exprdate=datetime.date(y1,m1,d1)
           currenDate=date.today()
           if(currenDate>exprdate):
            messageforExpiry=f"""Hello! {nameofclint} \nYour plan is Expired at {exprdate} Renew it As Soon As Possible \nThank You!!! \nFor More Detail Contact Us"""
            pywhatkit.sendwhatmsg_instantly(phone,messageforExpiry,wait_time=15)
    except:
        pass
def SendMessageOnWhatsAppforRemider():
    con=mysql.connector.connect(host="localhost",port="1073",user="root",
    password="Catbox@@7383",database="userid")
    cur10=con.cursor()
    try:
       cur10.execute("select expDate, phoneNumber,ClientName from inseringData")
       for i in cur10:
           expireValue,phone,nameOfReminder=i[0],i[1],i[2]
           d1,d2,m1,m2,y1,y2,y3,y4=int(expireValue[0]),int(expireValue[1]),int(expireValue[3]),int(expireValue[4]),int(expireValue[6]),int(expireValue[7]),int(expireValue[8]),int(expireValue[9])
           d1,m1,y1=int("%d%d" % (d1,d2)),int("%d%d" % (m1,m2)),int("%d%d%d%d" % (y1,y2,y3,y4))
           exprdate=datetime.date(y1,m1,d1)
           dayCalculating=exprdate-timedelta(days=4)
           currenDate=date.today()
           if(currenDate>=dayCalculating and currenDate<=exprdate):
            msgforRemider=f"""Hello! {nameOfReminder}\nYour Plan is Expiring Soon at {exprdate}\nContact Us to update Your Plan\nThank you!!!"""
            adnan10=pywhatkit.sendwhatmsg_instantly(phone,msgforRemider,wait_time=10)
    except:
        pass
btn1=CTkButton(home,text="Add NewClient",fg_color="#007FFF",  hover_color="#8B2323",text_color="white",font=("Arial", 14, "bold"), corner_radius=10,width=150,height=35,command=AddEmployee1,bg_color="white")
btn1.place(x=15,y=8)
#btn1.bind("<Enter>",hoverButton)
btn2=CTkButton(home,text="Show Details",fg_color="#007FFF",  hover_color="#8B2323",text_color="white",font=("Arial", 14, "bold"), corner_radius=10,width=150,height=35,command=fetchingData,bg_color="white")
btn2.place(x=15,y=50)
btn3=CTkButton(home,text="Update Detail",fg_color="#007FFF",  hover_color="#8B2323",text_color="white",font=("Arial", 14, "bold"), corner_radius=10,width=150,height=35,command=UpdateDetails,bg_color="white")
btn3.place(x=15,y=92)
expired=CTkButton(home,text="Expired Plan",fg_color="#007FFF",  hover_color="#8B2323",text_color="white",font=("Arial", 14, "bold"), corner_radius=10,width=150,height=35,command=lambda:ExpiredPlan(),bg_color="white")
expired.place(x=15,y=134)
def enquireFun():
    global useridEntry101,receiptEntry101,nameEntry101,phoneEntry101,DisplayWind2
    DisplayWind2=CTkToplevel()
    DisplayWind2.geometry("700x570+340+50")
    DisplayWind2.grab_set()
    DisplayWind2.title("Displaying Client's Data",)
    DisplayWind2.resizable(False,False)
    DisplayWind2.configure(fg_color="#7A8B8B")
    secondFrame=CTkFrame(DisplayWind2,fg_color="white",width=700,height=570)
    secondFrame.place(x=0,y=40)
    lb1=Label(DisplayWind2,text="Enquiry of New Client",bg="#7A8B8B",fg="blue",font=("arial",15,))
    lb1.pack(pady=6)
    userid=CTkLabel(DisplayWind2,text="Client Name:",font=("arial",16),fg_color="white",bg_color="white")
    userid.place(x=70,y=60)
    useridEntry101=CTkEntry(DisplayWind2,width=240,font=("arial",15),border_width=1,text_color='black',bg_color="white",border_color="blue",)
    useridEntry101.place(x=230,y=60)
    receipt=CTkLabel(DisplayWind2,text="Phone Number:",font=("arial",16),fg_color="white",bg_color="white")
    receipt.place(x=70,y=100)
    receiptEntry101=CTkEntry(DisplayWind2,width=240,font=("arial",15),border_width=1,text_color='black',bg_color="white",border_color="blue",)
    receiptEntry101.place(x=230,y=100)
    name=CTkLabel(DisplayWind2,text="Client Age:",font=("arial",16),fg_color="white",bg_color="white")
    name.place(x=70,y=140)
    nameEntry101=CTkEntry(DisplayWind2,width=240,font=("arial",15),border_width=1,text_color='black',bg_color="white",border_color="blue",)
    nameEntry101.place(x=230,y=140)
    phone=CTkLabel(DisplayWind2,text="Client Feedback:",font=("arial",16),fg_color="white",bg_color="white")
    phone.place(x=70,y=180)
    phoneEntry101=CTkEntry(DisplayWind2,width=240,font=("arial",16),border_width=1,text_color='black',bg_color="white",border_color="blue",)
    phoneEntry101.place(x=230,y=180)
    submitforfeed=CTkButton(DisplayWind2,text="Save",bg_color="white",fg_color="red",font=("arial",30,),text_color="white"
    ,cursor="hand2",width=120,command=savedata)
    submitforfeed.place(x=205,y=250)
    showDatailsforfeed=CTkButton(DisplayWind2,text="Details",bg_color="white",fg_color="green",font=("arial",30,),text_color="white"
    ,cursor="hand2",width=120,command=DetailsOfClient)
    showDatailsforfeed.place(x=380,y=250)
def DetailsOfClient():
        DisplayWind2.destroy()
        Detailswindo=CTkToplevel()
        Detailswindo.geometry("800x570+340+50")
        Detailswindo.grab_set()
        Detailswindo.title("Enquiry Details")
        Detailswindo.resizable(False,False)
        Detailswindo.configure(fg_color="#7A8B8B")
        tree2=ttk.Treeview(Detailswindo,columns=("0","1","2","3"),height=39,)
        tree2.place(x=0,y=40)
        tree2['show']='headings'
        tree2.heading(0,text="ClientName")
        tree2.heading(1,text="PhoneNumber")
        tree2.heading(2,text="ClientAge")
        tree2.heading(3,text="FeedBack")
        styl1=ttk.Style(Detailswindo)
        styl1.theme_names()
        styl1.theme_use('clam')
        styl1.configure(".",font=("arial",10))
        styl1.configure("Treeview.Heading", font=(None,11),)
        tree2.column("0",width=300,minwidth=55,stretch=False)
        tree2.column("1",width=250,minwidth=80)
        tree2.column("2",width=250,minwidth=250)
        tree2.column("3",width=400,minwidth=110)
        scrollbar2=ttk.Scrollbar(Detailswindo)
        scrollbar2.pack(side=RIGHT,fill=Y,pady=59,) 
        tree2.configure(yscrollcommand=scrollbar2.set)
        scrollbar2.configure(command=tree2.yview)
        try:
           con=mysql.connector.connect(host="localhost",port="1073",user="root",password="Catbox@@7383",database="userid")
           cur=con.cursor()
           cur.execute("select * from enquiry")
        except:
           pass
        z=0
        for ro in cur:
          tree2.insert('',z,text="\n",values=(ro[0],ro[1],ro[2],ro[3]))
          
def savedata():
    value1,value2,value3,value4=useridEntry101.get(),receiptEntry101.get(),nameEntry101.get(),phoneEntry101.get()
    valueforquery=(value1,value2,value3,value4)
    if(useridEntry101.get()=="" or phoneEntry101.get()=="" or receiptEntry101.get()=="" or nameEntry101.get()==""):
        messagebox.showerror("ERROR","Please Enter Data in All Fields")
    else:
      con=mysql.connector.connect(host="localhost",port="1073",user="root",
      password="Catbox@@7383",database="userid")
      cur10=con.cursor()
      cur10.execute("create table if not exists enquiry(name varchar(50),phoneNumber varchar(14),clentage int,feedback varchar(100))")
      query1="insert into enquiry(name,phoneNumber,clentage,feedback) values(%s,%s,%s,%s)"
      cur10.execute(query1,valueforquery)
      con.commit()
      messagebox.showinfo("Success","Data Inserted Successfuly")
Enquary=CTkButton(home,text="AddEnquiry",fg_color="#007FFF",  hover_color="#8B2323",text_color="white",font=("Arial", 14, "bold"), corner_radius=10,width=150,height=35,bg_color="white",command=enquireFun)
Enquary.place(x=15,y=176)
Backup=CTkButton(home,text="Data Backup",fg_color="#007FFF",  hover_color="#8B2323",text_color="white",font=("Arial", 14, "bold"), corner_radius=10,width=150,height=35,bg_color="white",command=BackupFun)
Backup.place(x=15,y=218)
def ClientRemindersFun():
    emptyTable,totalexpired=0,0
    DisplayWindclient=CTkToplevel()
    DisplayWindclient.geometry("850x570+360+55")
    DisplayWindclient.grab_set()
    DisplayWindclient.title("Client Reminder")
    DisplayWindclient.resizable(False,False)
    DisplayWindclient.configure(fg_color="#7A8B8B")
    mainfrm=LabelFrame(DisplayWindclient,bg="white",bd=0)
    canvas=Canvas(mainfrm)
    canvas.pack(side=LEFT,fill=BOTH,expand=1)
    scroolbar=ttk.Scrollbar(mainfrm,orient="vertical",command=canvas.yview)  
    scroolbar.pack(side = RIGHT, fill = Y)
    canvas.configure(yscrollcommand=scroolbar.set)
    canvas.bind("<Configure>",lambda e:canvas.configure(scrollregion=canvas.bbox("all")))
    seconframe=Frame(canvas)
    seconframe.pack()
    canvas.create_window((0,0),window=seconframe,anchor="nw")
    mainfrm.place(x=10,y=45,width=1255,height=750)
    sfram=Frame(seconframe,width=1200,height=40,bg="#242B64")
    sfram.pack(padx=12,pady=0)
    klable=Label(sfram,text="UserId",fg="white",bg="#242B64",font=('arial', 11,"bold"))
    klable.place(x=0,y=4)
    klable1=Label(sfram,text="ClientName",fg="white",bg="#242B64",font=('arial', 11,"bold"))
    klable1.place(x=80,y=4)
    klable2=Label(sfram,text="PhoneNumber",fg="white",bg="#242B64",font=('arial', 11,"bold"))
    klable2.place(x=400,y=4)
    klable2=Label(sfram,text="ClientAge",fg="white",bg="#242B64",font=('arial', 11,"bold"))
    klable2.place(x=600,y=4)
    klable2=Label(sfram,text="ExpiryDate",fg="white",bg="#242B64",font=('arial', 11,"bold"))
    klable2.place(x=750,y=4)
    RemainingLable=Label(sfram,text="RemainingDay",fg="white",bg="#242B64",font=('arial', 11,"bold"))
    RemainingLable.place(x=910,y=4)
    klable2=Label(sfram,text="Status",fg="white",bg="#242B64",font=('arial', 11,"bold"))
    klable2.place(x=1100,y=4)
    msgButton1=CTkButton(DisplayWindclient,text="SendMessageOnWhatsApp",font=("Verdana",12),fg_color="green",text_color="white",command=SendMessageOnWhatsAppforRemider)
    msgButton1.place(x=300,y=536)
    cy1=0
    def fun10():  
        global cy1
        sfram=Frame(seconframe,width=300,height=25,bg="black")
        sfram.pack(pady=5)
        if(cy1==0):
            cy1=10
            sfram.config(bg="green",)
            klable=Label(sfram,text=f"Userid",fg="white",bg="green")
            klable.place(x=0,y=0)
            klable1=Label(sfram,text=f"Client Name",fg="white",bg="green")
            klable1.place(x=80)
        else:
            klable=Label(sfram,text=f"Adnan",fg="white",bg="black")
            klable.place(x=0,y=0)
            klable1=Label(sfram,text=f"Kalam",fg="white",bg="black")
            klable1.place(x=80)
            print("Value",cy1)
    con=mysql.connector.connect(host="localhost",port="1073",user="root",
    password="Catbox@@7383",database="userid")
    cur10=con.cursor()
    try:
       cur10.execute("select userid,clientName,phoneNumber,clientAge,expDate from inseringData")
    except:
        pass
    for getdat1 in cur10:
        emptyTable=10
        useridexp,clientNameexp,phoneNumberexp,clientAgeexp,expDateexp=getdat1[0],getdat1[1],getdat1[2],getdat1[3],getdat1[4]
        d1,d2,m1,m2,y1,y2,y3,y4=int(expDateexp[0]),int(expDateexp[1]),int(expDateexp[3]),int(expDateexp[4]),int(expDateexp[6]),int(expDateexp[7]),int(expDateexp[8]),int(expDateexp[9])
        d1,m1,y1=int("%d%d" % (d1,d2)),int("%d%d" % (m1,m2)),int("%d%d%d%d" % (y1,y2,y3,y4))
        exprdate=datetime.date(y1,m1,d1)
        RemaingDay=exprdate-timedelta(days=4)
        #print(exprdate,RemaingDay)
        currenDate=date.today()
        if(currenDate>=RemaingDay and currenDate<=exprdate):
            findingDay=exprdate-currenDate
            resulday=findingDay.days
            totalexpired=totalexpired+1
            sfram=Frame(seconframe,width=1200,height=35,bg="#A9A9A9")
            sfram.pack(padx=25,pady=1)
            klable=Label(sfram,text=useridexp,fg="black",bg="#A9A9A9",font=("times now",11))
            klable.place(x=0,y=4)
            klable1=Label(sfram,text=clientNameexp,fg="black",bg="#A9A9A9",font=("times now",11))
            klable1.place(x=80,y=4)
            klable2=Label(sfram,text=phoneNumberexp,fg="black",bg="#A9A9A9",font=("times now",11))
            klable2.place(x=400,y=4)
            klable2=Label(sfram,text=clientAgeexp,fg="black",bg="#A9A9A9",font=("times now",11))
            klable2.place(x=602,y=4)
            klable2=Label(sfram,text=expDateexp,fg="black",bg="#A9A9A9",font=("times now",11))
            klable2.place(x=750,y=4)
            remainingLable=Label(sfram,text=f"Days {resulday}",fg="red",bg="#A9A9A9",font=("times now",11))
            remainingLable.place(x=910,y=4)
            klable2=Label(sfram,text="Active",fg="Yellow",bg="#A9A9A9",font=("times now",11))
            klable2.place(x=1100,y=4)
    if(emptyTable==0):
        ValueLable=Label(DisplayWindclient,text="No Registered Record Found",fg="#FFFF00",font=("verdana",13,"bold"),bg="#7A8B8B")
        ValueLable.place(x=295,y=3)
    else:
        ValueLable=Label(DisplayWindclient,text=f"Total Client is in expiring Soon: {totalexpired}",fg="#FFFF00",font=("verdana",13,"bold"),bg="#7A8B8B")
        ValueLable.place(x=420,y=1)
    DisplayWindclient.mainloop()
clintReminder=CTkButton(home,text="ClientReminder",fg_color="#007FFF",  hover_color="#8B2323",text_color="white",font=("Arial", 14, "bold"), corner_radius=10,width=150,height=35,bg_color="white",command= ClientRemindersFun)
clintReminder.place(x=15,y=260)
home.mainloop()