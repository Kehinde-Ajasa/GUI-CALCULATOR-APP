from tkinter import *

calculator = Tk()

windows = Entry(calculator, width=42, borderwidth=5, background='#b2beb5')
windows.grid(row=0, column=0, columnspan=4)
calculator.title('CALCULATOR')


def addition(value):
	recent = windows.get()
	windows.delete(0, END)
	windows.insert(0, str(recent) + str(value))
	return

def clear():
	windows.delete(0, END)


def add():
	global first_number
	first_number = windows.get()
	global number
	global operation
	operation = 'addition'
	number = float(first_number)
	windows.delete(0, END)

def subtract():
	global first_number
	first_number = windows.get()
	global subtract
	global operation
	operation = 'subtraction'
	subtract = float(first_number)
	windows.delete(0, END)

def multiply():
	global first_number
	first_number = windows.get()
	global multiply
	global operation
	operation = 'multiply'
	multiply = float(first_number)
	windows.delete(0, END)

def divide():
	global first_number
	first_number = windows.get()
	global divide
	global operation
	operation = 'divide'
	divide = float(first_number)
	windows.delete(0, END)

def delete():
	global first_number
	first_number = windows.get()
	delete = first_number
	windows.delete(0, END)
	windows.insert(0, delete[:-1])

def percent():
	global first_number
	first_number = windows.get()
	global percent
	global operation
	operation = 'percentage'
	percent = float(first_number)
	windows.delete(0, END)

def point():
	windows.insert(windows.get(), '.')


def equal():
	second_number = windows.get()
	windows.delete(0, END)
	if operation == 'addition':
		windows.insert(0, (number + float(second_number)))
	elif operation == 'subtraction':
		windows.insert(0, (subtract - float(second_number)))
	elif operation == 'multiply':
		windows.insert(0, multiply * (float(second_number)))
	elif operation == 'divide':
		windows.insert(0, divide/(float(second_number)))
	elif operation == 'percentage':
		windows.insert(0, float((percent)/100))


button_1 = Button(calculator, text='1', padx=24, pady=10, command= lambda:addition(1), background='black', fg='white')
button_2 = Button(calculator, text='2', padx=25, pady=10, command=lambda:addition(2), background='black', fg='white')
button_3 = Button(calculator, text='3', padx=25, pady=10, command=lambda:addition(3), background='black', fg='white')
button_4 = Button(calculator, text='4', padx=24, pady=10, command=lambda:addition(4), background='black', fg='white')
button_5 = Button(calculator, text='5', padx=25, pady=10, command=lambda:addition(5), background='black', fg='white')
button_6 = Button(calculator, text='6', padx=25, pady=10, command=lambda:addition(6), background='black', fg='white')
button_7 = Button(calculator, text='7', padx=24, pady=10, command=lambda:addition(7), background='black', fg='white')
button_8 = Button(calculator, text='8', padx=25, pady=10, command=lambda:addition(8), background='black', fg='white')
button_9 = Button(calculator, text='9', padx=25, pady=10, command=lambda:addition(9), background='black', fg='white')
button_0 = Button(calculator, text='0', padx=25, pady=10, command=lambda:addition(0), background='black', fg='white')
button_C = Button(calculator, text='C', padx=23, pady=10, command=clear, background='black', fg='white')
button_divide = Button(calculator, text='/', padx=25, pady=10, command=divide, background='black', fg='white')
button_multiply = Button(calculator, text='x ', padx=24.4, pady=10, command=multiply, background='black', fg='white')
button_add = Button(calculator, text='+', padx=25, pady=10, command=add, background='black', fg='white')
button_subtract = Button(calculator, text='-', padx=26, pady=10, command=subtract, background='black', fg='white')
button_cancel = Button(calculator, text='del', padx=20, pady=10, command=delete, background='black', fg='white')
button_equal = Button(calculator, text='=', padx=25, pady=32, command=equal, background='black', fg='white')
button_percent = Button(calculator, text='%', padx=22, pady=10, command=percent, background='black', fg='white')
button_point = Button(calculator, text='. ', padx=25, pady=10, command=point, background='black', fg='white')

button_C.grid(row=1, column=0)
button_divide.grid(row=1, column=1)
button_multiply.grid(row=1, column=2)
button_cancel.grid(row=1, column=3)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_subtract.grid(row=2, column=3)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_add.grid(row=3, column=3)

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_equal.grid(row=4, column=3, rowspan=2)

button_percent.grid(row=5, column=0)
button_0.grid(row=5, column=1)
button_point.grid(row=5, column=2)

calculator.mainloop()