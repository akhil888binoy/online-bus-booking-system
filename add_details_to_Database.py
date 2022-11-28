from tkinter import *
import tkinter.messagebox
root=Tk()
h,w= root.winfo_screenheight(), root.winfo_screenwidth()
root.geometry('%dx%d+0+0' %(w,h))
def p1():
    root.destroy()
    import Main_Menu
def p2():
    root.destroy()
    import Bus_details
def p3():
    root.destroy()
    import Bus_running_details
def p4():
    root.destroy()
    import Operator_details
img =PhotoImage(file='.\\Bus_for_project.png')
root.title('online booking system')
Label(root, image=img).grid(row=0,columnspan=11)
Label(root, text='Online bus booking', font='Arial 30 bold',bg='light coral', fg='white').grid(row=1,column=1, padx=700, columnspan=10)
Label(root, text='Add New Details to Database', font='Arial 20 bold',fg='blue').grid(row=2,column=1, pady=40, columnspan=10)
Button(root, text='New Operator',font='Arial 10 bold', bg='red', fg='white', command= p4).grid(row=3, column =0, pady=10, columnspan=10)
Button(root, text='New Bus',font='Arial 10 bold', bg='green', fg='white', command=p2).grid(row=3, column =1, pady=10, columnspan=10)
Button(root, text='New Run',font='Arial 10 bold', bg='pink', fg='white', command= p3).grid(row=3, column =2, pady=10, columnspan=10)
Button(root, text='Home',font='Arial 10 bold', bg='purple', fg='white', command=p1).grid(row=3, column =3, pady=10, columnspan=10)

root.mainloop()
