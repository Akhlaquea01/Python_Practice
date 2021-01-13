from tkinter import *
import parser

firoz=Tk()
firoz.title("My first GUI")

i = 0
def clear_all():#use for clear entry box
    display.delete(0, END)

def get_variables(num):#use for entry
    global i
    display.insert(i, num)
    i += 1

def get_operation(operator):#use for perform the opration
    global i
    length = len(operator)
    display.insert(i, operator)
    i += length

def undo():#use for remove last opration
    whole_string = display.get()
    if len(whole_string):
        new_string = whole_string[:-1]
        print(new_string)
        clear_all()
        display.insert(0, new_string)
    else:
        clear_all() 
        display.insert(0, "Error, press AC")

def calculate():
    
    whole_string = display.get()
    try:
        formulae = parser.expr(whole_string).compile()
        result = eval(formulae)
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0, "Error!")

display = Entry(firoz, font = ("Alex Brush", 25),bd=5,bg="green")
display.grid(row = 0,column=0, columnspan = 6, sticky = W+E)

#t1=Entry(firoz,font=20,bd=10,bg="green",justify=RIGHT)
#t1.grid(row=0,column=0,columnspan=6,sticky=W+E)

b1=Button(firoz,text="1", command = lambda : get_variables(1),bg="red",bd=5,fg="white",font=10,height=2,width=5,activebackground="yellow")
b1.grid(row=1,column=0)

b1=Button(firoz,text="2", command = lambda : get_variables(2),bg="red",bd=5,fg="white",font=10,height=2,width=5)
b1.grid(row=1,column=1)

b1=Button(firoz,text="3", command = lambda : get_variables(3),bg="red",bd=5,fg="white",font=10,height=2,width=5)
b1.grid(row=1,column=2)

b1=Button(firoz,text="4", command = lambda : get_variables(4),bg="red",bd=5,fg="white",font=10,height=2,width=5)
b1.grid(row=2,column=0)

b1=Button(firoz,text="5", command = lambda : get_variables(5),bg="red",bd=5,fg="white",font=10,height=2,width=5)
b1.grid(row=2,column=1)

b1=Button(firoz,text="6", command = lambda : get_variables(6),bg="red",bd=5,fg="white",font=10,height=2,width=5)
b1.grid(row=2,column=2)

b1=Button(firoz,text="7", command = lambda : get_variables(7),bg="red",bd=5,fg="white",font=10,height=2,width=5)
b1.grid(row=3,column=0)

b1=Button(firoz,text="8", command = lambda : get_variables(8),bg="red",bd=5,fg="white",font=10,height=2,width=5)
b1.grid(row=3,column=1)

b1=Button(firoz,text="9", command = lambda : get_variables(9),bg="red",bd=5,fg="white",font=10,height=2,width=5)
b1.grid(row=3,column=2)

b1=Button(firoz,text="0", command = lambda : get_variables(0),bg="red",bd=5,fg="white",font=10,height=2,width=5,activebackground="yellow")
b1.grid(row=4,column=0)


cls = Button(firoz, text = "AC", command = clear_all,height=2,width=5,bg="black",bd=5,fg="white",font=10,activebackground="yellow" )
cls.grid(row = 1, column = 4)
##zero.grid(row = 5, column = 0)
point = Button(firoz, text = ".",height=2,width=5, command = lambda : get_operation("."),bg="black",bd=5,fg="white",font=10,activebackground="yellow")
point.grid(row = 4, column = 1)
result = Button(firoz, text = "=", command = calculate,height=2,width=5,bg="black",bd=5,fg="white",font=10,activebackground="yellow")
result.grid(row = 4, column =4,columnspan=2,ipadx=30)

plus = Button(firoz, text = "+", command =  lambda : get_operation("+"), height=2,width=5,bg="black",bd=5,fg="white",font=10,activebackground="yellow")
plus.grid(row = 4, column = 3)
minus = Button(firoz, text = "-", command =  lambda : get_operation("-"),height=2,width=5,bg="black",bd=5,fg="white",font=10,activebackground="yellow")
minus.grid(row = 3, column = 3)
multiply = Button(firoz,text = "*",command =  lambda : get_operation("*"),height=2,width=5,bg="black",bd=5,fg="white",font=10,activebackground="yellow")
multiply.grid(row = 2, column = 3)
divide = Button(firoz, text = "/", command = lambda :  get_operation("/"),height=2,width=5,bg="black",bd=5,fg="white",font=10,activebackground="yellow")
divide.grid(row = 1, column = 3)
modulo = Button(firoz, text = "%", command = lambda :  get_operation("%"),height=2,width=5,bg="black",bd=5,fg="white",font=10,activebackground="yellow")
modulo.grid(row = 4, column = 2)
left_bracket = Button(firoz, text = "(", command = lambda: get_operation("("),height=2,width=5,bg="black",bd=5,fg="white",font=10,activebackground="yellow")
left_bracket.grid(row = 2, column = 4)
undo_button = Button(firoz, text = "C", command = undo,height=2,width=5,bg="black",bd=5,fg="white",font=10,activebackground="yellow")
undo_button.grid(row = 1, column =5 )
sqrt = Button(firoz, text = " √", command = lambda:get_operation("**(1/2.0)"),height=2,width=5,bg="black",bd=5,fg="white",font=10,activebackground="yellow")
sqrt.grid(row = 3, column = 4)
right_bracket = Button(firoz, text = ")",command = lambda: get_operation(")"), height=2,width=5,bg="black",bd=5,fg="white",font=10,activebackground="yellow")
right_bracket.grid(row = 2, column = 5)
square = Button(firoz, text = "x^2", command = lambda: get_operation("**2"),height=2,width=5,bg="black",bd=5,fg="white",font=10,activebackground="yellow")
square.grid(row = 3, column = 5)



firoz.mainloop()
