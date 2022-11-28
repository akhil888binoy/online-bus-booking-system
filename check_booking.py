from tkinter import *
from tkinter.messagebox import *
root=Tk()
h,w= root.winfo_screenheight(), root.winfo_screenwidth()
root.geometry('%dx%d+0+0' %(w,h))
def p1():
    root.destroy()
    import Main_Menu
def p2():
    if mobile_no.get()=='':
        showerror('Error','Add mobile number')
    
    
img =PhotoImage(file='.\\Bus_for_project.png')
root.title('online booking system')
Label(root, image=img).grid(row=0,column=0,columnspan=11)
Label(root, text='Online bus booking', font='Arial 30 bold',bg='light coral', fg='white').grid(row=1,column=0,columnspan=10, padx=700)
Label(root, text='Check your Booking', font='Arial 20 bold',bg='blue', fg='white').grid(row=2,column=0,columnspan=10, pady=40)
Label(root, text='Enter Mobile Number', font='Arial 15 bold',bg='blue', fg='white').grid(row=3,column=0, pady=10, columnspan=9)
mobile_no=Entry(root)
mobile_no.grid(row=3,column=1, columnspan=10)
Button(root, text='Check booking',font='Arial 10 bold', bg='red', fg='white',command=p2).grid(row=3, column =3, pady=10, columnspan=10)
Button(root, text='Home',font='Arial 10 bold', bg='purple', fg='white',command=p1 ).grid(row=9, column =3, pady=30, columnspan=10)

root.mainloop()
