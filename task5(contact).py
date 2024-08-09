from tkinter import *
from tkinter import messagebox,ttk
import mysql.connector as sq

sql=sq.connect(host='localhost',user='root',password='1234')
cur=sql.cursor()
cur.execute('create database if not exists contact;')
cur.execute('use contact')
cur.execute('create table if not exists contact(name varchar(30),phone bigint primary key,email varchar(40),address varchar(100));')

def add1():
    u=(x1.get(),x2.get(),x3.get(),x4.get())
    cur.execute('insert into contact values'+str(u))
    sql.commit()
    messagebox.showinfo('contact','Contact Added Sucessfully..!')
    bck()

def add():
    win.withdraw()
    global win1,x1,x2,x3,x4,bt
    win1=Tk()
    win1.geometry('550x550+300+50')
    win1.title('Contact')
    win1.configure(bg='pink')
    Label(win1,text='ADD CONTACT',font=('courier',30,'italic'),bg='pink',fg='blue').pack(pady=10)
    Label(win1,text='NAME',font=('courier',22,'italic'),bg='pink',fg='black').pack()
    x1=Entry(win1,width=30,font=('arial',20))
    x1.pack(pady=10)
    Label(win1,text='PHONE NUMBER',font=('courier',22,'italic'),bg='pink',fg='black').pack()
    x2=Entry(win1,width=30,font=('arial',20))
    x2.pack(pady=10)
    Label(win1,text='EMAIL',font=('courier',22,'italic'),bg='pink',fg='black').pack()
    x3=Entry(win1,width=30,font=('arial',20))
    x3.pack(pady=10)
    Label(win1,text='ADDRESS',font=('courier',22,'italic'),bg='pink',fg='black').pack()
    x4=Entry(win1,width=35,font=('arial',18))
    x4.pack(pady=10)
    Button(win1,text='Submit',font=('courier',20,'italic'),bg='lavender',fg='red',activeforeground='orange',command=add1).pack(pady=10)
    Button(win1,text='Back',font=('courier',16,'italic'),bg='lavender',fg='red',activeforeground='orange',command=bck).place(x=450,y=500)
    win1.mainloop()

def bck():
    try:
        win2.destroy()
        win.deiconify()
    except:
        win1.withdraw()
        win.deiconify()
    
def search(s):
    cur.execute('select * from contact where phone='+str(s.get()))
    m=cur.fetchone()
    for item in tt.get_children():
       tt.delete(item)
    tt.insert('',END,values=m)

def view():
    global tt,win1
    win.withdraw()
    win1=Tk()
    win1.geometry('800x400+300+200')
    win1.title('Contact')
    win1.configure(bg='pink')
    Label(win1,text='VIEW CONTACT',font=('courier',30,'italic'),bg='pink',fg='blue').place(x=250,y=20)
    Label(win1,text='Mobile No.:',font=('courier',17,'italic'),bg='pink',fg='black').place(x=120,y=70)
    e1=Entry(win1,font=('arial',16))
    e1.place(x=280,y=70)
    Button(win1,text='Search',font=('courier',14,'italic'),bg='lavender',fg='red',activeforeground='orange',command=lambda:search(e1)).place(x=550,y=65)
    style=ttk.Style()
    style.theme_use('clam')
    style.configure('Treeview.Heading',bg="green3",font=('courier',25,'bold'),foreground='red')
    style.configure('Treeview',font=('Perpetua Titling MT',15,),height=10)
    tt=ttk.Treeview(win1, column=(1,2,3,4),show='headings', height=10)
    tt.column("#1", anchor=CENTER,width=130)
    tt.heading("#1", text="NAME")
    tt.column("#2", anchor=CENTER,width=120)
    tt.heading("#2", text="PHONE No.")
    tt.column("#3", anchor=CENTER,width=220)
    tt.heading("#3", text="E-MAIL")
    tt.column("#4", anchor=CENTER,width=230)
    tt.heading("#4", text="ADDRESS")
    cur.execute('select * from contact;')
    m=cur.fetchall()
    tt.insert('',END,values=('','','',''))
    for j in m:
        tt.insert('',END,values=j)
    tt.place(x=50,y=110)
    Button(win1,text='Back',font=('courier',16,'italic'),bg='lavender',fg='red',activeforeground='orange',command=bck).place(x=710,y=345)
    win1.mainloop()


def upd1():
    cur.execute('update contact set '+x+"='"+e2.get()+"' where phone='"+e1.get()+"';")
    sql.commit()
    messagebox.showinfo('contact','Contact Modified Sucessfully..!')
    bck()

def upd():
    global x,e2
    x=var.get()
    win1.withdraw()
    global win2
    win2=Toplevel()
    #win2.attributes('-topmost' , 1)
    win2.geometry('600x350+300+100')
    win2.title('Contact')
    win2.configure(bg='pink')
    Label(win2,text='MODIFY CONTACT',font=('courier',30,'italic'),bg='pink',fg='blue').place(x=150,y=40)
    ll=Label(win2,text='New '+x.title(),font=('courier',19,'bold'),bg='pink',fg='black')
    ll.place(x=60,y=150)
    e2=Entry(win2,font=('arial',16),width=20)
    e2.place(x=250,y=150)
    Button(win2,text='Modify',font=('courier',17,'bold'),bg='lavender',fg='red',activeforeground='purple',command=upd1).place(x=360,y=220)
    Button(win2,text='Back',font=('courier',16,'italic'),bg='lavender',fg='red',activeforeground='purple',command=bck).place(x=500,y=300)
    win2.mainloop()

def update():
    global win1,e1,radio,ll,b1
    win.withdraw()
    win1=Toplevel()
    win1.attributes('-topmost' , 1)
    win1.geometry('600x400+300+100')
    win1.title('Contact')
    win1.configure(bg='pink')
    Label(win1,text='MODIFY CONTACT',font=('courier',30,'italic'),bg='pink',fg='blue').place(x=150,y=10)
    ll=Label(win1,text='Mobile No.:',font=('courier',19,'bold'),bg='pink',fg='black')
    ll.place(x=60,y=90)
    e1=Entry(win1,font=('arial',16))
    e1.place(x=250,y=90)
    Label(win1,text=" Select  The  Field To Modify:",font=('courier',18,'bold'),fg='purple',bg='pink').place(x=30,y=160)
    Button(win1,text='Back',font=('courier',16,'italic'),bg='lavender',fg='red',command=bck).place(x=500,y=350)
    global var
    var=StringVar()
    radio=Radiobutton(win1,text='Name',font=('courier',19,'bold') ,variable=var,value='name',bg='pink',fg='#304618',activebackground='#c7dcd4',activeforeground='black')
    radio.place(x=150,y=200)
    radio=Radiobutton(win1,text='E-Mail',font=('courier',19,'bold') ,variable=var,value='email',bg='pink',fg='#304618',activebackground='#c7dcd4',activeforeground='black')
    radio.place(x=300,y=200)
    radio=Radiobutton(win1,text='Address',font=('courier',19,'bold') ,variable=var,value='address',bg='pink',fg='#304618',activebackground='#c7dcd4',activeforeground='black')
    radio.place(x=220,y=250)
    var.set(' ')
    b1=Button(win1,text='Modify',font=('courier',17,'bold'),bg='lavender',fg='red',command=upd)
    b1.place(x=360,y=300)
    win1.mainloop()
    
def dlt(s):
    cur.execute('delete from contact where phone='+str(s.get()))
    sql.commit()
    messagebox.showinfo('contact','Contact Deleted Sucessfully..!')
    bck()
    

def delete():
    global win1
    win.withdraw()
    win1=Tk()
    win1.geometry('600x350+300+200')
    win1.title('Contact')
    win1.configure(bg='pink')
    Label(win1,text='DELETE CONTACT',font=('courier',30,'italic'),bg='pink',fg='blue').place(x=150,y=20)
    Label(win1,text='Mobile No.:',font=('courier',17,'italic'),bg='pink',fg='black').place(x=60,y=150)
    e1=Entry(win1,font=('arial',16))
    e1.place(x=250,y=150)
    Button(win1,text='Delete',font=('courier',14,'italic'),bg='lavender',fg='red',command=lambda:dlt(e1)).place(x=370,y=210)
    Button(win1,text='Back',font=('courier',16,'italic'),bg='lavender',fg='red',command=bck).place(x=500,y=300)
    win1.mainloop()

win=Tk()
win.geometry('500x450+300+100')
win.title('Contact')
win.configure(bg='lavender')
Label(win,text='CONTACT BOOK',font=('courier',28,'italic'),bg='lavender',fg='blue').place(x=100,y=30)
Button(win,text='ADD',font=('courier',20,'italic'),bg='aqua',fg='red',activeforeground='purple',width=10,command=add).place(x=150,y=100)
Button(win,text='VIEW',font=('courier',20,'italic'),bg='aqua',fg='red',activeforeground='purple',width=10,command=view).place(x=150,y=180)
Button(win,text='UPDATE',font=('courier',20,'italic'),bg='aqua',fg='red',width=10,activeforeground='purple',command=update).place(x=150,y=260)
Button(win,text='DELETE',font=('courier',20,'italic'),bg='aqua',fg='red',width=10,activeforeground='purple',command=delete).place(x=150,y=340)
win.mainloop()
