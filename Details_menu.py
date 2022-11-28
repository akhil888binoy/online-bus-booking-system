from tkinter import *
from tkinter.messagebox import *
root=Tk()
h,w= root.winfo_screenheight(), root.winfo_screenwidth()
root.geometry('%dx%d+0+0' %(w,h))
def p1():
    root.destroy()
    import Main_Menu
def p2():
    if To.get()=='':
        showerror("Error", "enter To")
    elif From.get()=='':
        showerror("Error", "enter From")
    elif jnr_date.get()=='':
        showerror("Error", "enter Journey date")
    else:
        import Bus_details
    
img =PhotoImage(file='.\\Bus_for_project.png')
root.title('online booking system')
Label(root, image=img).grid(row=0,column=0,columnspan=11)
Label(root, text='Online bus booking', font='Arial 30 bold',bg='light coral', fg='white').grid(row=1,column=0,columnspan=10, padx=700)
Label(root, text='Enter bus Details', font='Arial 15 bold',bg='Blue', fg='white').grid(row=2,column=0,columnspan=10, pady=40)
Label(root, text = 'TO', font = 'calibre 10 bold').grid(row=3,column=0, pady=10,columnspan=9) 
To= Entry(root)
To.grid(row=3,column=1,columnspan=10)
Label(root, text = 'FROM', font = 'calibre 10 bold').grid(row=4,column=0, pady=10,columnspan=9) 
From= Entry(root)
From.grid(row=4,column=1,columnspan=10)
Label(root, text = 'Journey Date', font = 'calibre 10 bold').grid(row=5,column=0, pady=10,columnspan=9) 
jnr_date=Entry(root)
jnr_date.grid(row=5,column=1,columnspan=10)
Button(root, text='Show bus',font='Arial 10 bold', bg='green', fg='white',command=p2).grid(row=6, column =0, pady=10, columnspan=10)
Button(root, text='Home',font='Arial 10 bold', bg='red', fg='white',command=p1).grid(row=6, column =1, pady=10, columnspan=10)


