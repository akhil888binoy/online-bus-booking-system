from tkinter import *
from tkinter.messagebox import *
import sqlite3

con= sqlite3.Connection('BUS')
cur=con.cursor()
cur.execute('create table if not exists operator(Op_id int, name varchar(30), address varchar(25), phone int, email varchar(30))')
root=Tk()
h,w= root.winfo_screenheight(), root.winfo_screenwidth()
root.geometry('%dx%d+0+0' %(w,h))
img =PhotoImage(file='.\\Bus_for_project.png')
def p1():
    root.destroy()
    import Main_Menu
def p2():
    if name.get()=='':
        showerror('Error','Please enter name')
    elif address.get()=='':
        showerror('Error', 'Please enter address')
    elif phone.get()=='':
        showerror('Error', 'Please enter phone')
    elif email.get()=='':
        showerror('Error', 'Please enter email')
    elif Op_id.get()=='':
        showerror('Error', 'Please enter operator id')
    else:
        cur.execute('insert into operator (Op_id, name, address, phone, email) values(?,?,?,?,?)', (Op_id.get(), name.get(), address.get(), phone.get(), email.get()))
        con.commit()
        showinfo("online bus booking system", "operator Added")
def p3():
    if name.get()=='':
        showerror('Error','Please enter name')
    elif address.get()=='':
        showerror('Error', 'Please enter address')
    elif phone.get()=='':
        showerror('Error', 'Please enter phone')
    elif email.get()=='':
        showerror('Error', 'Please enter email')
    elif Op_id.get()=='':
        showerror('Error', 'Please enter operator id')
    else:
        showinfo("online bus booking system", "operator Updated")
root.title('online booking system')
Label(root, image=img).grid(row=0,columnspan=11)
Label(root, text='Online bus booking', font='Arial 30 bold',bg='light coral', fg='white').grid(row=1,column=1, padx=700, columnspan=10)
Label(root, text='Add bus operator details', font='Arial 15 bold',bg='Blue', fg='white').grid(row=2,column=1, pady=40,columnspan=10)
Label(root, text = 'Operator ID', font = 'calibre 10 bold').grid(row=3,column=1,padx=40, columnspan=9) 
Op_id= Entry(root)
Op_id.grid(row=3,column=2,padx=400, columnspan=10)
Label(root, text = 'Name', font = 'calibre 10 bold').grid(row=4,column=1, pady=5,padx=400, columnspan=9) 
name= Entry(root)
name.grid(row=4,column=2,padx=400, columnspan=10)
Label(root, text = 'Address', font = 'calibre 10 bold').grid(row=5,column=1, pady=5,padx=400, columnspan=9) 
address=Entry(root)
address.grid(row=5,column=2,padx=400, columnspan=10)
Label(root, text = 'Phone', font = 'calibre 10 bold').grid(row=6,column=1, pady=5,padx=400, columnspan=9) 
phone=Entry(root)
phone.grid(row=6,column=2,padx=400, columnspan=10)
Label(root, text = 'Email', font = 'calibre 10 bold').grid(row=7,column=1, pady=5,padx=400, columnspan=9) 
email= Entry(root)
email.grid(row=7,column=2,padx=400, columnspan=10)
Button(root, text='Add',font='Arial 10 bold', bg='green', fg='white', command=p2).grid(row=8, column=1, pady=10, columnspan=10)
Button(root, text='Edit',font='Arial 10 bold', bg='red', fg='white', command=p3).grid(row=8, column=2, pady=10, columnspan=10)
Button(root, text='Home',font='Arial 10 bold', bg='purple', fg='white', command=p1).grid(row=8, column=3, pady=10, columnspan=10)
root.mainloop()
