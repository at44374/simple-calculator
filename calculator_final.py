from tkinter import *
from math import *
window = Tk()
window.title("Simple Calculator")
entry = Entry(window, width=55, borderwidth=5, bg="red")
entry.grid(row=0, column=0, columnspan=4)


def click_num(number):
    comment = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(comment)+str(number))


def click_clear():
    entry.delete(0, END)


def click_add():
    first_num = entry.get()
    entry.delete(0, END)
    global f_num
    f_num = float(first_num)
    global math
    math = "add"


def click_sin():
    first_num = entry.get()
    entry.delete(0, END)
    s = (float(first_num)* 2 * pi) / 360
    entry.insert(0, sin(s))


def click_cos():
    first_num = entry.get()
    entry.delete(0, END)
    s = (float(first_num) * 2 * pi) / 360
    entry.insert(0, cos(s))


def click_tan():
    first_num = entry.get()
    entry.delete(0, END)
    s = (float(first_num) * 2 * pi) / 360
    entry.insert(0, tan(s))


def click_sqrt():
    first_num = entry.get()
    entry.delete(0, END)
    s=float(first_num)
    entry.insert(0, sqrt(s))


def click_subtract():
    first_num = entry.get()
    entry.delete(0, END)
    global f_num
    f_num = float(first_num)
    global math
    math = "subtract"


def click_multiply():
    first_num = entry.get()
    entry.delete(0, END)
    global f_num
    f_num = float(first_num)
    global math
    math = "multiply"


def click_devide():
    first_num = entry.get()
    entry.delete(0, END)
    global f_num
    f_num = float(first_num)
    global math
    math = "devide"


def click_equal():
    second_number = entry.get()
    entry.delete(0, END)
    if math == "add":
        entry.insert(0, f_num+float(second_number))
    if math == "subtract":
        entry.insert(0, f_num-float(second_number))
    if math == "multiply":
        entry.insert(0, f_num*float(second_number))
    if math == "devide":
        entry.insert(0, f_num/float(second_number))


button_1 = Button(window, text="1", padx=55, pady=20, command=lambda: click_num(1), fg="violet red")
button_2 = Button(window, text="2", padx=55, pady=20, command=lambda: click_num(2), fg="violet red")
button_3 = Button(window, text="3", padx=55, pady=20, command=lambda: click_num(3), fg="violet red")
button_4 = Button(window, text="4", padx=55, pady=20, command=lambda: click_num(4), fg="violet red")
button_5 = Button(window, text="5", padx=55, pady=20, command=lambda: click_num(5), fg="violet red")
button_6 = Button(window, text="6", padx=55, pady=20, command=lambda: click_num(6), fg="violet red")
button_7 = Button(window, text="7", padx=55, pady=20, command=lambda: click_num(7), fg="violet red")
button_8 = Button(window, text="8", padx=55, pady=20, command=lambda: click_num(8), fg="violet red")
button_9 = Button(window, text="9", padx=55, pady=20, command=lambda: click_num(9), fg="violet red")
button_0 = Button(window, text="0", padx=55, pady=20, command=lambda: click_num(0), fg="violet red")
button_dot = Button(window, text=".", padx=55, pady=20, command=lambda: click_num('.'), fg="violet red")
button_clear = Button(window, text="C", padx=55, pady=85, command=click_clear)
button_add = Button(window, text="+", padx=55, pady=20, command=click_add)
button_subtract = Button(window, text="-", padx=55, pady=20, command=click_subtract)
button_devide = Button(window, text="/", padx=55, pady=20, command=click_devide)
button_multiply = Button(window, text="*", padx=55, pady=20, command=click_multiply)
button_equal = Button(window, text="=", padx=59, pady=55, command=click_equal)
button_sin = Button(window, text="sin", padx=55, pady=20, command=click_sin)
button_cos = Button(window, text="cos", padx=55, pady=20, command=click_cos)
button_tan = Button(window, text="tan", padx=55, pady=20, command=click_tan)
button_sqrt = Button(window, text="√", padx=59, pady=20, command=click_sqrt)


button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_clear.grid(row=4, column=2, rowspan=3)
button_0.grid(row=4, column=1)
button_dot.grid(row=4, column=0)
button_add.grid(row=5, column=0)
button_subtract.grid(row=5, column=1)
button_multiply.grid(row=6, column=0)
button_devide.grid(row=6, column=1)
button_equal.grid(row=5, column=3, rowspan=2)
button_sin.grid(row=1, column=3)
button_cos.grid(row=2, column=3)
button_tan.grid(row=3, column=3)
button_sqrt.grid(row=4, column=3)


window.mainloop()
