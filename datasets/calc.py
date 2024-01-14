from tkinter import *
top = Tk() 
def add():
	result = float(e1.get()) + float(e2.get())
	l.config(text='Result:'+str(result))
def sub():
	result = float(e1.get()) - float(e2.get())
	l.config(text='Result:'+str(result))
def div():
	result = float(e1.get()) / float(e2.get())
	l.config(text='Result:'+str(result))
def mul():
	result = float(e1.get()) * float(e2.get())
	l.config(text='Result:'+str(result))

	
top.geometry('500x300')
l1 = Label(top, text='Number1:', font=('Courier',15))
l1.place(x=10,y=10)
l2 = Label(top, text='Number2:', font=('Courier',15))
l2.place(x=10,y=80)
e1 = Entry(top, font=('Courier',15))
e1.place(x=125,y=10)
e2 = Entry(top, font=('Courier',15))
e2.place(x=125,y=80)
B1 = Button(top,text ="ADD", command=add)
B1.place(height=40, width=80, x=20, y=150)
B2 = Button(top,text ="SUB", command=sub)
B2.place(height=40, width=80, x=120, y=150)
B3 = Button(top,text ="DIV", command=div)
B3.place(height=40, width=80, x=220, y=150)
B4 = Button(top,text ="MUL", command=mul)
B4.place(height=40, width=80, x=320, y=150)
l = Label(text='Result:',font=('Courier',15))
l.place(x=150, y=200)
top.mainloop()
