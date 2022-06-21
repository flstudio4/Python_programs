""" Created by Dmitrii Sumenko, 6/20/2022
    The program calculates total of starting
    balance + interest, that compounded monthly """

from tkinter import *

window = Tk()
window.title("Compound Interest Calculator")
window.geometry("400x250")
window.config(bg="#b8c1c2")

frame1 = Frame(window, bg="#b8c1c2")
frame1.pack()
frame = Frame(window, bg="#b8c1c2")
frame.pack()


def calculate():
    balance = float(p.get())
    percent = float(r.get()) / 100
    time = float(n.get()) / 12
    result = balance * (1 + (percent / 12)) ** (12 * time)
    string = f"Your total is: ${round(result, 2)}"
    result_label.configure(text=string)


def clear():
    interest.delete(0, END)
    principal.delete(0, END)
    period.delete(0, END)
    result_label.configure(text="")


p = StringVar()  # period
r = StringVar()  # interest
n = StringVar()  # period

principal_label = Label(frame1, text="Starting amount", bg="#b8c1c2")
principal_label.grid(column=0, row=0, padx=20, pady=5, sticky=W)
principal = Entry(frame1, textvariable=p)
principal.grid(column=1, row=0, padx=20, pady=5)
interest_label = Label(frame1, text="Annual interest rate", bg="#b8c1c2")
interest_label.grid(column=0, row=1, padx=20, pady=5, sticky=W)
interest = Entry(frame1, textvariable=r)
interest.grid(column=1, row=1, padx=20, pady=5)
period_label = Label(frame1, text="Period in months", bg="#b8c1c2")
period_label.grid(column=0, row=2, padx=20, pady=5, sticky=W)
period = Entry(frame1, textvariable=n)
period.grid(column=1, row=2, padx=20, pady=5)
result_button = Button(frame1, text="Calculate", command=calculate)
result_button.grid(column=0, row=3, pady=5, padx=20, sticky=W)
clear_button = Button(frame1, text="Clear", command=clear)
clear_button.grid(column=1, row=3, padx=20, pady=15)
result_label = Label(frame, text="", font=("Arial", 10, "bold"), bg="#b8c1c2")
result_label.pack(padx=15, pady=10)
legal_label = Label(frame, text="Dmitrii Sumenko design, 2022", font=("Arial", 10), bg="#b8c1c2", state=DISABLED)
legal_label.pack(padx=15, pady=15)

window.mainloop()
