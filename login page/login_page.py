from tkinter import *

root=Tk()
root.geometry("400x400")
root.title("project 1")
root.config(background="grey")


titlelable=Label( root,text="Login Page", font=("Roboto",15), bg="grey", fg="black")
titlelable.grid(row=0, column=0, columnspan=2 )

inlabel=Label(root, text="Username", font=("Roboto", 15), bg="red")
inlabel.grid(row=1,column=0 , padx=20, pady=20)

inbox=Entry(root)
inbox.grid(row=1, column=1)


inlabel=Label(root, text="Password", font=("Roboto", 15), bg="red")
inlabel.grid(row=2,column=0 , padx=20, pady=20)

inbox=Entry(root)
inbox.grid(row=2, column=1)






root.mainloop()


