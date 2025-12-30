from tkinter import*
root=Tk()
e=Entry(root,width=36)
e.grid(row=0,column=0,columnspan=3)



#defining commands 


def number_display(number):
	x=e.get()
	e.delete(0,END)
	e.insert(0,x+ str(number))
def equalto():
	if command_to_run=="multiplication":
		x=int(float(first_number))*int(e.get())
		e.delete(0,END)
		e.insert(0,x)
	if command_to_run=="addition":
		x=int(float(first_number))+int(e.get())
		e.delete(0,END)
		e.insert(0,x)
	if command_to_run=="subtraction":
		x=int(float(first_number))-int(e.get())
		e.delete(0,END)
		e.insert(0,x)
	if command_to_run=="division":
		x=int(float(first_number))/int(e.get())
		e.delete(0,END)
		e.insert(0,x)

def add ():
	global command_to_run
	global first_number
	command_to_run="addition"
	first_number=e.get()
	e.delete(0,END)

def subtract():
	global command_to_run
	global first_number
	command_to_run="subtraction"
	first_number=e.get()
	e.delete(0,END)

	

def multiplication():
	global command_to_run
	global first_number
	command_to_run="multiplication"
	first_number=e.get()
	e.delete(0,END)

	

def  division():
	global command_to_run
	global first_number
	command_to_run="division"
	first_number=e.get()
	e.delete(0,END)

def clear():
	global command_to_run
	global first_number
	e.delete(0,END)




#defininig buttons
button_7=Button(root,text="7",command=lambda: number_display(7),padx=30,pady=20)
button_8=Button(root,text="8",command=lambda: number_display(8),padx=30,pady=20)
button_9=Button(root,text="9",command=lambda: number_display(9),padx=30,pady=20)

button_4=Button(root,text="4",command=lambda: number_display(4),padx=30,pady=20)
button_5=Button(root,text="5",command=lambda: number_display(5),padx=30,pady=20)
button_6=Button(root,text="6",command=lambda: number_display(6),padx=30,pady=20)

button_1=Button(root,text="1",command=lambda: number_display(1),padx=30,pady=20)
button_2=Button(root,text="2",command=lambda: number_display(2),padx=30,pady=20)
button_3=Button(root,text="3",command=lambda: number_display(3),padx=30,pady=20)

button_0=Button(root,text="0",command=lambda: number_display(0),padx=106,pady=20)

button_equal=Button(root,text="=",command=equalto ,padx=30,pady=20,width=12)
button_add=Button(root,text="+",command=add ,padx=30,pady=20)


button_multiply=Button(root,text="X",command=multiplication ,padx=30,pady=20)
button_divide=Button(root,text="/",command=division ,padx=30,pady=20)
button_subtract=Button(root,text="-",command=subtract ,padx=30,pady=20)

button_clear=Button(root,text="clear",command=clear ,padx=97,pady=20)

#buttons on screen 
button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_0.grid(row=4,column=0,columnspan=3)

button_equal.grid(row=5,column=1,columnspan=2)
button_add.grid(row=5,column=0)

button_multiply.grid(row=6,column=0)
button_divide.grid(row=6,column=1)
button_subtract.grid(row=6,column=2)

button_clear.grid(row=7,column=0,columnspan=3)


root.mainloop()

