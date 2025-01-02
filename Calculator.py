from tkinter import *

# Global variables
first_number = second_number = operator = None

# Handle digit input
def get_digit(digit):
    current = result_label['text']
    if current == "":  # Handle empty input
        new = str(digit)
    else:
        new = current + str(digit)
    result_label.config(text=new)

# Clear the display
def clear():
    result_label.config(text="")

# Handle operator input
def get_operator(op):
    global first_number, operator
    try:
        first_number = int(result_label['text'])
        operator = op
        result_label.config(text="")
    except ValueError:
        result_label.config(text="Error")

# Calculate the result
def get_result():
    global first_number, operator
    try:
        second_number = int(result_label['text'])
        if operator == "+":
            result_label.config(text=str(first_number + second_number))
        elif operator == "-":
            result_label.config(text=str(first_number - second_number))
        elif operator == "*":
            result_label.config(text=str(first_number * second_number))
        elif operator == "/":
            if second_number == 0:
                result_label.config(text="Error")  # Division by zero error
            else:
                result_label.config(text=str(first_number / second_number))
        operator = None
    except ValueError:
        result_label.config(text="Error")

# Main root window
root = Tk()
root.title("Calculator")
root.geometry('280x380')
root.resizable(0, 0)
root.configure(background='black')

# Display label
result_label = Label(root, text='', bg="black", fg="white", anchor="e")
result_label.grid(row=0, column=0, columnspan=4, pady=(20, 10), sticky='w')
result_label.config(font=('Verdana', 30, 'bold'))

# Row 1
btn7 = Button(root, text='7', bg='#00a65a', fg='white', width=5, height=2, command=lambda: get_digit(7))
btn7.grid(row=1, column=0)
btn7.config(font=('Verdana', 14))

btn8 = Button(root, text='8', bg='#00a65a', fg='white', width=5, height=2, command=lambda: get_digit(8))
btn8.grid(row=1, column=1)
btn8.config(font=('Verdana', 14))

btn9 = Button(root, text='9', bg='#00a65a', fg='white', width=5, height=2, command=lambda: get_digit(9))
btn9.grid(row=1, column=2)
btn9.config(font=('Verdana', 14))

btn_add = Button(root, text='+', bg='#00a65a', fg='white', width=5, height=2, command=lambda: get_operator('+'))
btn_add.grid(row=1, column=3)
btn_add.config(font=('Verdana', 14))

# Row 2
btn4 = Button(root, text='4', bg='#00a65a', fg='white', width=5, height=2, command=lambda: get_digit(4))
btn4.grid(row=2, column=0)
btn4.config(font=('Verdana', 14))

btn5 = Button(root, text='5', bg='#00a65a', fg='white', width=5, height=2, command=lambda: get_digit(5))
btn5.grid(row=2, column=1)
btn5.config(font=('Verdana', 14))

btn6 = Button(root, text='6', bg='#00a65a', fg='white', width=5, height=2, command=lambda: get_digit(6))
btn6.grid(row=2, column=2)
btn6.config(font=('Verdana', 14))

btn_sub = Button(root, text='-', bg='#00a65a', fg='white', width=5, height=2, command=lambda: get_operator('-'))
btn_sub.grid(row=2, column=3)
btn_sub.config(font=('Verdana', 14))

# Row 3
btn1 = Button(root, text='1', bg='#00a65a', fg='white', width=5, height=2, command=lambda: get_digit(1))
btn1.grid(row=3, column=0)
btn1.config(font=('Verdana', 14))

btn2 = Button(root, text='2', bg='#00a65a', fg='white', width=5, height=2, command=lambda: get_digit(2))
btn2.grid(row=3, column=1)
btn2.config(font=('Verdana', 14))

btn3 = Button(root, text='3', bg='#00a65a', fg='white', width=5, height=2, command=lambda: get_digit(3))
btn3.grid(row=3, column=2)
btn3.config(font=('Verdana', 14))

btn_mult = Button(root, text='*', bg='#00a65a', fg='white', width=5, height=2, command=lambda: get_operator('*'))
btn_mult.grid(row=3, column=3)
btn_mult.config(font=('Verdana', 14))

# Row 4
btn_clr = Button(root, text='C', bg='#00a65a', fg='white', width=5, height=2, command=clear)
btn_clr.grid(row=4, column=0)
btn_clr.config(font=('Verdana', 14))

btn0 = Button(root, text='0', bg='#00a65a', fg='white', width=5, height=2, command=lambda: get_digit(0))
btn0.grid(row=4, column=1)
btn0.config(font=('Verdana', 14))

btn_equ = Button(root, text='=', bg='#00a65a', fg='white', width=5, height=2, command=get_result)
btn_equ.grid(row=4, column=2)
btn_equ.config(font=('Verdana', 14))

btn_div = Button(root, text='/', bg='#00a65a', fg='white', width=5, height=2, command=lambda: get_operator('/'))
btn_div.grid(row=4, column=3)
btn_div.config(font=('Verdana', 14))
root.mainloop()
