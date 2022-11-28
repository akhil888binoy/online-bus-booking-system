from tkinter import*
root=Tk() 
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
def p1():
    root.destroy()
    import Details_menu
def p2():
    root.destroy()
    import Bus_details
def p3():
    root.destroy()
    import check_booking 
img=PhotoImage(file='.\\Bus_for_project.png')
root.title('online booking system')
Label(root,image=img).grid(row=0,column=0,columnspan=4,pady=20)
Label(root,text='Online Bus Booking System',font='Arial 35 bold',bg='sky blue',fg='red').grid(row=1,column=0,columnspan=5,padx=600)
Button(root,text='Seat Booking',font='Arial 15 bold',bg='Blue', fg='white', command= p1).grid(row=2,column=0,padx=150,pady=70)
Button(root,text='Check Booked Seat',font='Arial 15 bold',bg='Purple', fg='white', command=p3).grid(row=2,column=1)
Button(root,text='Add Bus Details',font='Arial 15 bold',bg='Red', fg='white', command=p2 ).grid(row=2,column=2,padx=200)
Label(root,text='For Admins only',font='Arial 15 bold',fg='red').grid(row=3,column=2)


root.mainloop()
