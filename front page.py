from tkinter import *
root=Tk()
h,w= root.winfo_screenheight(), root.winfo_screenwidth()
root.geometry('%dx%d+0+0' %(w,h))
def close():
    root.destroy()
    import Main_Menu
img =PhotoImage(file='.\\Bus_for_project.png')
root.title('online booking system')
Label(root, image=img).grid(row=0,columnspan=6)
Label(root, text='Online bus booking', font='Arial 30 bold',bg='light coral', fg='white').grid(row=1,column=0, padx=700)
Label(root, text='Name: Akhil Binoy', font ='Arial 15 bold', fg='purple2').grid(row=2, column=0, pady=30)
Label(root, text='Er: 211B031', font ='Arial 15 bold', fg='purple2').grid(row=3, column=0, pady=10)
Label(root, text='Mobile : 234567890098', font ='Arial 15 bold', fg='purple2').grid(row=4, column=0, pady=30)
Label(root, text='Submitted To : Dr Mahesh Kumar ', font='Arial 20 bold',bg='light coral', fg='white').grid(row=5,column=0, pady=10)
Label(root, text='Project Based Learning', font ='Arial 20 bold', fg='purple2').grid(row=6, column=0)
root.after(5000,close)
