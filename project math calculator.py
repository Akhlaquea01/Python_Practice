from tkinter import *
import parser

root = Tk()
root.title('Calculator')

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

root.columnconfigure(0,pad=2)
root.columnconfigure(1,pad=2)
root.columnconfigure(2,pad=2)
root.columnconfigure(3,pad=2)
root.columnconfigure(4,pad=2)

root.rowconfigure(0,pad=10)
root.rowconfigure(1,pad=10)
root.rowconfigure(2,pad=10)
root.rowconfigure(3,pad=10)

display = Entry(root, font = ("Calibri", 20))
display.grid(row = 1, columnspan = 6, sticky = W+E)

one = Button(root, text = "7",height=1,width=3, command = lambda : get_variables(7), font=("Calibri", 20))
one.grid(row = 2, column = 0)
two = Button(root, text = "8",height=1,width=3, command = lambda : get_variables(8), font=("Calibri", 20))
two.grid(row = 2, column = 1)
         
three = Button(root, text = "9",height=1,width=3, command = lambda : get_variables(9), font=("Calibri",20))
three.grid(row = 2, column = 2)

four = Button(root, text = "4",height=1,width=3, command = lambda : get_variables(4), font=("Calibri", 20))
four.grid(row = 3 , column = 0)
five = Button(root, text = "5",height=1,width=3,command = lambda : get_variables(5), font=("Calibri", 20))
five.grid(row = 3, column = 1)
six = Button(root, text = "6",height=1,width=3, command = lambda : get_variables(6), font=("Calibri", 20))
six.grid(row = 3, column = 2)

seven = Button(root, text = "1",height=1,width=3, command = lambda : get_variables(1), font=("Calibri", 20))
seven.grid(row = 4, column =0)
eight = Button(root, text = "2",height=1,width=3, command = lambda : get_variables(2), font=("Calibri", 20))
eight.grid(row = 4, column =1)
nine = Button(root , text = "3",height=1,width=3, command = lambda : get_variables(3), font=("Calibri", 20))
nine.grid(row = 4,column =2)

cls = Button(root, text = "AC",height=1,width=3, command = clear_all, font=("Calibri", 20))
cls.grid(row = 2, column = 4)
zero = Button(root, text = "0", height=1,width=3,command = lambda : get_variables(0), font=("Calibri", 20))
zero.grid(row = 5, column = 0)
point = Button(root, text = ".",height=1,width=3, command = lambda : get_operation("."), font=("Calibri", 20))
point.grid(row = 5, column = 1)
result = Button(root, text = "=",height=1,width=3, command = calculate, font=("Calibri", 20),foreground="green")
result.grid(row = 5, column = 5)

plus = Button(root, text = "+", height=1,width=3,command =  lambda : get_operation("+"), font=("Calibri", 20))
plus.grid(row = 5, column = 3)
minus = Button(root, text = "-",height=1,width=3, command =  lambda : get_operation("-"), font=("Calibri", 20))
minus.grid(row = 4, column = 3)
multiply = Button(root,text = "*", height=1,width=3,command =  lambda : get_operation("*"), font=("Calibri", 20))
multiply.grid(row = 3, column = 3)
divide = Button(root, text = "/",height=1,width=3, command = lambda :  get_operation("/"), font=("Calibri", 20))
divide.grid(row = 2, column = 3)
modulo = Button(root, text = "%",height=1,width=3, command = lambda :  get_operation("%"), font=("Calibri", 20))
modulo.grid(row = 5, column = 2)
left_bracket = Button(root, text = "(",height=1,width=3, command = lambda: get_operation("("), font =("Calibri", 20))
left_bracket.grid(row = 3, column = 4)
undo_button = Button(root, text = "C",height=1,width=3, command = undo, font =("Calibri", 20))
undo_button.grid(row = 2, column =5 )
sqrt = Button(root, text = " √",height=1,width=3, command = lambda:get_operation("**(1/2.0)"), font=("Calibri", 20))
sqrt.grid(row = 4, column = 4,pady=4)
right_bracket = Button(root, text = ")", height=1,width=3,command = lambda: get_operation(")"), font =("Calibri",20))
right_bracket.grid(row = 3, column = 5)
square = Button(root, text = "x^2",height=1,width=3, command = lambda: get_operation("**2"), font = ("Calibri", 20))
square.grid(row = 4, column = 5)

root.mainloop()
