from tkinter import *

root=Tk()
root.geometry("500x500")
root.title("project 1")
root.config(background="white")


titlelable=Label( root,text="CALENDER", font=("times new roman",50), bg="navy", fg="white")
titlelable.grid(row=0, column=0, columnspan=2 )

inlabel=Label(root, text="Enter Year", font=("times new roman", 25), bg="black")
inlabel.grid(row=1,column=0 , padx=20, pady=20)

inbox=Entry(root)
inbox.grid(row=1, column=1)


yesbutton=Button(root, text="Enter", font=("times new roman", 20), bg="black")
yesbutton.grid(row=2, column=1)




root.mainloop()


