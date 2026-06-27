from tkinter import *
from tkinter import font

def conversion():
    errorlable.grid_forget()
    try:
        C=float(inbox.get())
        F=(C*1.8)+ 32
        Anslable.config(text=str(F)+ "F" )
        Anslable.grid(row=3, column=0, columnspan=2)
    except ValueError:
        Anslable.config(text="")
        errorlable.grid(row=3, column=0, columnspan=2)
  

root=Tk()
root.geometry("500x500")
root.title("Converter")
root.config(background="#ebb2ae")



titlelable=Label(root, text="Celcius -> Farenheit", font=("Playbill", 50, "italic"), bg="#ebb2ae" )
titlelable.grid(row=0,column=0,columnspan=2)

Celinput=Label(root, text="Enter degrees =" , font=("Google Sans Flex", 20), bg="#e0dfdc")
Celinput.grid(row=1, column=0, pady=20)



inbox=Entry(root)
inbox.grid(row=1, column=1, pady=20)

convertb=Button(root, text="Convert", font=("Google Sans Flex", 20), bg="#e0dfdc", command=conversion)
convertb.grid(row=2, column=0, columnspan=2, pady=20)


Anslable=Label(root, font=("Google Sans Flex", 20), bg="#e0dfdc")

errorlable=Label(root, text="enter valid input", font=("Google Sans Flex", 20), bg="#e0dfdc")



root.mainloop()