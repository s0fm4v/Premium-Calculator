import tkinter
from tkinter import ttk  # arxh
from ttkthemes import ThemedTk


def clear():  # pou tha bei sto koumpi clear
    global result
    result = ""
    var.set(result)  # grafw sto entry to result


def equal():  # pou tha bei sto koumpi =
    try:
        global result
        calculate = eval(result)
        var.set(calculate)
        result = str(calculate)
    except ZeroDivisionError:
        result = "ERROR"
        var.set(result)


def press(number):  # pou tha bei se ola ta upoloipa koumpia, command= lambda: press(1)
    global result
    result += str(number)
    if result=='error':
        result = ' '
    var.set(result)


result = ""  # to periexomeno tou entry

win = ThemedTk(theme="adapta")
win.configure(themebg="adapta")
win.title("Premium Calculator")  # titlos parathyrou
win.geometry('385x230')  # megethos parathyrou
var = tkinter.StringVar()  # o typos ton periexomenvn tou entry tha einai panta string
e = ttk.Entry(win, width=45, textvariable=var)
e.grid(column=0, row=0, columnspan=4)

btn1 = ttk.Button(win, text="1", width=12, command=lambda: press(1))
btn0 = ttk.Button(win, text="0", width=12, command=lambda: press(0))
btn2 = ttk.Button(win, text="2", width=12, command=lambda: press(2))
btn3 = ttk.Button(win, text="3", width=12, command=lambda: press(3))
btn4 = ttk.Button(win, text="4", width=12, command=lambda: press(4))
btn5 = ttk.Button(win, text="5", width=12, command=lambda: press(5))
btn6 = ttk.Button(win, text="6", width=12, command=lambda: press(6))
btn7 = ttk.Button(win, text="7", width=12, command=lambda: press(7))
btn8 = ttk.Button(win, text="8", width=12, command=lambda: press(8))
btn9 = ttk.Button(win, text="9", width=12, command=lambda: press(9))
btnplus = ttk.Button(win, text="+", width=12, command=lambda: press("+"))
btnminus = ttk.Button(win, text="-", width=12, command=lambda: press("-"))
btnequals = ttk.Button(win, text="=", width=12, command=equal)
btntimes = ttk.Button(win, text="x", width=12, command=lambda: press("*"))
btndia = ttk.Button(win, text="/", width=12, command=lambda: press("/"))
btnpar1 = ttk.Button(win, text="(", width=12, command=lambda: press("("))
btnpar2 = ttk.Button(win, text=")", width=12, command=lambda: press(")"))
btndnm = ttk.Button(win, text="^", width=12, command=lambda: press("**"))
btnclear = ttk.Button(win, text="Clear", width=12, command=clear)
btncomma = ttk.Button(win, text=",", width=12, command=lambda: press("."))
btn1.grid(row=1, column=0)
btn2.grid(row=1, column=1)
btn3.grid(row=1, column=2)
btnplus.grid(row=1, column=3)
btn4.grid(row=2, column=0)
btn5.grid(row=2, column=1)
btn6.grid(row=2, column=2)
btnminus.grid(row=2, column=3)
btn7.grid(row=3, column=0)
btn8.grid(row=3, column=1)
btn9.grid(row=3, column=2)
btntimes.grid(row=3, column=3)
btnequals.grid(row=4, column=0)
btndia.grid(row=4, column=1)
btnpar1.grid(row=4, column=2)
btnpar2.grid(row=4, column=3)
btndnm.grid(row=5, column=0)
btnclear.grid(row=5, column=1)
btncomma.grid(row=5, column=2)
btn0.grid(row=5, column=3)
win.mainloop()
