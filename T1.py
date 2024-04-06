from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import *

root = Tk()
root.title("Time Convertor")
root.iconbitmap("Time.ico") #ICON
root.geometry("1100x500+50+50")
root.config(bg="lightblue")
f = ("Calibri", 20 , "bold")


#title
title_label = Label(root, text="Time Converter", font=("Arial", 25, "bold"), bg="black", fg="lightblue")
title_label.place(x=400, y=30)

#convertion dropdown
convert_label = Label(root, text="Change Convertion Format :", font = f)
convert_label.place(x=100, y=100)

convert_menu_var = StringVar()
convert_menu_var.set("Hours to Seconds")
convert_menu = OptionMenu(root, convert_menu_var, "Hours to Seconds", "Seconds to Hours")
convert_menu.config(font=("Calibri", 20), bg="lightgray", width=15)
convert_menu.place(x=550, y=100)

#Input 
lab = Label(root, text="Enter the Value : ", font = f )
lab.place(x=100 ,y=200)
ent = Entry(root, font = f)
ent.place(x=550, y=200)

#Covertion
def convert():
	try:
		format = convert_menu_var.get()
		time = ent.get().strip()

		if not time: #empty Validation
			raise ValueError(" --Time cannot be empty!-- ")

		time = float(time)

		if format == "Hours to Seconds":
			if time < 0:
				raise ValueError(" --Hours cannot be Negative(-ve)!!!-- ")
			else:
				seconds = time * 3600
				result.config(text = str(time) + " hour is  equal to " + str(seconds) + " seconds.")

		elif format == "Seconds to Hours":
			if time < 0:
				raise ValueError(" --Seconds cannot be Negative(-ve)!!!-- ")
			else:
				hours = time / 3600
				result.config(text = str(time) + " seconds is  equal to " + str(hours) + " hours.")
			
		else:
			raise ValueError("Invalid Format")
			
	except Exception as e:
		showerror("Error : ", str(e))


#Result button
btn = Button(root, text="Convert", font = f, command=convert)
btn.place(x=450, y=300)

#Result
result = Label(root, text= "", font = f, bg="lightblue", fg="black")
result.place(x=300, y=400)

#exit msg box
def on_closing():
	if askyesno("Quit","Do you want to exit???"):
		root.destroy()
root.protocol("WM_DELETE_WINDOW", on_closing)


root.mainloop()


