from tkinter import *
from tkinter.messagebox import *
import sqlite3

con= sqlite3.Connection('BUS')
cur=con.cursor()
cur.execute('create table if not exists running(bus1_id int, running_date date, seat_available int) ')
root=Tk()
h,w= root.winfo_screenheight(), root.winfo_screenwidth()
root.geometry('%dx%d+0+0' %(w,h))
def p1():
    root.destroy()
    import Main_Menu
def p2():
    if bus_id1.get()=='':
        showerror('Error','Please enter bus id')
    elif running_date.get()=='':
        showerror('Error', 'Please enter Running date')
    elif seat_available.get()=='':
        showerror('Error', 'Please enter seat available')
    else:
        cur.execute('insert into running (bus1_id, runing_date , seat_available) values(?,?,?) ',(bus1_id.get(), running_date.get(), seat_available.get()) )
        con.commit()
        showinfo("online bus booking system", "Bus Added")
def p3():
        showerror("welcome to bus booking system", " Run deleted " )

    
img =PhotoImage(file='.\\Bus_for_project.png')
root.title('online booking system')
Label(root, image=img).grid(row=0,columnspan=11)
Label(root, text='Online bus booking', font='Arial 30 bold',bg='light coral', fg='white').grid(row=1,column=1, padx=700, columnspan=10)
Label(root, text='Bus Running Details', font='Arial 15 bold',bg='Blue', fg='white').grid(row=2,column=1, pady=40, columnspan=10)
Label(root, text = 'Bus Id', font = 'calibre 10 bold').grid(row=3,column=1, pady=10,columnspan=9) 
bus_id1 = Entry(root)
bus_id1.grid(row=3,column=2,columnspan=10)
Label(root, text = 'Running Date', font = 'calibre 10 bold').grid(row=4,column=1, pady=5, columnspan=9) 
running_date=Entry(root)
running_date.grid(row=4,column=2, columnspan=10)
Label(root, text = 'Seat Available', font = 'calibre 10 bold').grid(row=5,column=1, pady=5, columnspan=9) 
seat_available=Entry(root)
seat_available.grid(row=5,column=2, columnspan=10)
Button(root, text='Add Run',font='Arial 10 bold', bg='green', fg='white', command=p2).grid(row=9, column =1, pady=30,columnspan=10)
Button(root, text='Delete Run',font='Arial 10 bold', bg='red', fg='white', command=p3).grid(row=9, column =2, pady=30, columnspan=10)
Button(root, text='Home',font='Arial 10 bold', bg='purple', fg='white',command=p1).grid(row=9, column =3, pady=30, columnspan=10)

root.mainloop()
