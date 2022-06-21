from tkinter import *
from tkinter import messagebox

#Use pillow for images
#from PIL import ImageTk, Image
#We will also be using the CTk library for better design at https://github.com/TomSchimansky/CustomTkinter

#Create the root window
root = Tk()
root.title("Program Name")
root.geometry("400x400");
root.iconbitmap('images/favicon.ico')

def popup():
	error = messagebox.showerror("Error 0x0000", "This application is not ready for use")

def inputBoxClick():
	inputVal = inputBox.get()
	Label(root,text=inputVal).pack()

inputBox = Entry(root, width = 100)
inputBox.pack()

Button(root,text="Start Creating", command=popup,padx=20,pady=20).pack()
#Run the main loop
root.mainloop()