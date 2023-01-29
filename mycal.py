import tkinter as tk

def buttonpress(num):
    global calculation
    calculation+=str(num)
    equationLabel.set(calculation)

def equals():
    try:
        global calculation
        total=str(eval(calculation))
        equationLabel.set(total)
        calculation=total
    except:
        equationLabel.set('error')
        calculation=''

def clear():
    global calculation
    equationLabel.set('')
    calculation=''

def deletelast():
    global calculation
    calculation=calculation[:-1]
    equationLabel.set(calculation)

calculation=''

window=tk.Tk()
window.geometry('500x600')
window.title('My_Calculator')

equationLabel = tk.StringVar()
label=tk.Label(window, textvariable=equationLabel, font=('consolas', 20), bg='white', height=3, width=40)
label.pack(padx=10, pady=10)

frame=tk.Frame(window)
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.columnconfigure(2 , weight=1)

button1=tk.Button(frame, text=7, height=5, width=9, command=lambda: buttonpress(7))
button1.grid(row=0, column=0, sticky=tk.W+tk.E)
button2=tk.Button(frame, text=8, height=5, width=9, command=lambda: buttonpress(8))
button2.grid(row=0, column=1, sticky=tk.W+tk.E)
button3=tk.Button(frame, text=9, height=5, width=9, command=lambda: buttonpress(9))
button3.grid(row=0, column=2, sticky=tk.W+tk.E)
multiply=tk.Button(frame, text='X', height=5, width=9, command=lambda: buttonpress('*'))
multiply.grid(row=0, column=3, sticky=tk.W+tk.E)


button4=tk.Button(frame, text=4, height=5, width=9, command=lambda: buttonpress(4))
button4.grid(row=1, column=0, sticky=tk.W+tk.E)
button5=tk.Button(frame, text=5, height=5, width=9, command=lambda: buttonpress(5))
button5.grid(row=1, column=1, sticky=tk.W+tk.E)
button6=tk.Button(frame, text=6, height=5, width=9, command=lambda: buttonpress(6))
button6.grid(row=1, column=2, sticky=tk.W+tk.E)
minus=tk.Button(frame, text='-', height=5, width=9, command=lambda: buttonpress('-'))
minus.grid(row=1, column=3, sticky=tk.W+tk.E)

button7=tk.Button(frame, text=1, height=5, width=9, command=lambda: buttonpress(1))
button7.grid(row=2, column=0, sticky=tk.W+tk.E)
button8=tk.Button(frame, text=2, height=5, width=9, command=lambda: buttonpress(2))
button8.grid(row=2, column=1, sticky=tk.W+tk.E)
button9=tk.Button(frame, text=3, height=5, width=9, command=lambda: buttonpress(3))
button9.grid(row=2, column=2, sticky=tk.W+tk.E)
plus=tk.Button(frame, text='+', height=5, width=9, command=lambda: buttonpress('+'))
plus.grid(row=2, column=3, sticky=tk.W+tk.E)

equal=tk.Button(frame, text='=', height=5, width=9, command= equals)
equal.grid(row=3, column=0, sticky=tk.W+tk.E)
button10=tk.Button(frame, text=0, height=5, width=9, command=lambda: buttonpress(0))
button10.grid(row=3, column=1, sticky=tk.W+tk.E)
decimal=tk.Button(frame, text='.', height=5, width=9, command=lambda: buttonpress('.'))
decimal.grid(row=3, column=2, sticky=tk.W+tk.E)
divide=tk.Button(frame, text='/', height=5, width=9, command=lambda: buttonpress('/'))
divide.grid(row=3, column=3, sticky=tk.W+tk.E)

clear=tk.Button(frame, text='clear', height=5, width=9, command= clear)
clear.grid(row=4, column=0, sticky=tk.W+tk.E)
dellast=tk.Button(frame, text='delete last digit', height=5, width=9, command=deletelast)
dellast.grid(row=4, column=1, sticky=tk.W+tk.E)

frame.pack(fill='x', padx=10, pady=10)


window.mainloop()
