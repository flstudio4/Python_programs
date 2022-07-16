from tkinter import *

string_length = 16
first_value = 0
second_value = 0
result = 0
is_dot_entered = False
multiplication_pressed = False
div_pressed = False
sum_pressed = False
subtraction_pressed = False
percent_pressed = False
equals_pressed = False
block = False
e = False


def button_1():
    if len(text_var.get()) < string_length and not block:
        value = text_var.get() + str(1)
        text_var.set(value)


def button_2():
    if len(text_var.get()) < string_length and not block:
        value = text_var.get() + str(2)
        text_var.set(value)


def button_3():
    if len(text_var.get()) < string_length and not block:
        value = text_var.get() + str(3)
        text_var.set(value)


def button_4():
    if len(text_var.get()) < string_length and not block:
        value = text_var.get() + str(4)
        text_var.set(value)


def button_5():
    if len(text_var.get()) < string_length and not block:
        value = text_var.get() + str(5)
        text_var.set(value)


def button_6():
    if len(text_var.get()) < string_length and not block:
        value = text_var.get() + str(6)
        text_var.set(value)


def button_7():
    if len(text_var.get()) < string_length and not block:
        value = text_var.get() + str(7)
        text_var.set(value)


def button_8():
    if len(text_var.get()) < string_length and not block:
        value = text_var.get() + str(8)
        text_var.set(value)


def button_9():
    if len(text_var.get()) < string_length and not block:
        value = text_var.get() + str(9)
        text_var.set(value)


def button_0():
    if text_var.get() != "-0" and text_var.get() != "0" and not block:
        if len(text_var.get()) < string_length:
            value = text_var.get() + str(0)
            text_var.set(value)


def button_plus_min():
    if len(text_var.get()) < string_length and text_var.get() == "" and not block:
        value = text_var.get() + str("-")
        text_var.set(value)


def button_dot():
    global is_dot_entered
    if len(text_var.get()) < string_length and not is_dot_entered and not block:
        value = text_var.get() + str(".")
        text_var.set(value)
        is_dot_entered = True


def common():
    global is_dot_entered
    if text_var.get() != "":
        global first_value
        first_value = float(text_var.get())
        text_var.set("")
    is_dot_entered = False


def button_percent():
    if not e:
        common()
        global block
        global percent_pressed
        percent_pressed = True
        block = False


def button_multiply():
    if not e:
        common()
        global block
        global multiplication_pressed
        multiplication_pressed = True
        block = False


def button_division():
    if not e:
        global block
        global div_pressed
        common()
        div_pressed = True
        block = False


def button_addition():
    if not e:
        global block
        global sum_pressed
        common()
        sum_pressed = True
        block = False


def button_distraction():
    if not e:
        common()
        global block
        global subtraction_pressed
        subtraction_pressed = True
        block = False


def button_C():
    global is_dot_entered
    global first_value
    global second_value
    global multiplication_pressed
    global div_pressed
    global sum_pressed
    global subtraction_pressed
    global percent_pressed
    global equals_pressed
    global block
    global e

    entry_field.delete(0, END)
    is_dot_entered = False
    second_value = 0
    first_value = 0
    multiplication_pressed = False
    div_pressed = False
    sum_pressed = False
    subtraction_pressed = False
    percent_pressed = False
    equals_pressed = False
    block = False
    e = False


def button_del():
    if not block and not e:
        entry_field.delete(len(text_var.get()) - 1, END)


def button_equals():
    global first_value
    global second_value
    global equals_pressed
    global multiplication_pressed
    global div_pressed
    global sum_pressed
    global subtraction_pressed
    global percent_pressed
    global block
    global e

    if not e:
        if text_var.get() == "":
            second_value = first_value
            block = True
        if text_var.get() != "":
            second_value = float(text_var.get())
            equals_pressed = True

        if multiplication_pressed:
            multiply()
            multiplication_pressed = False

        if div_pressed:
            division()
            div_pressed = False

        if sum_pressed:
            addition()
            sum_pressed = False

        if subtraction_pressed:
            subtraction()
            subtraction_pressed = False

        if percent_pressed:
            percentage()
            percent_pressed = False

        if equals_pressed:
            first_value = result
            equals_pressed = False
            block = True


def multiply():
    global result
    result = round((first_value * second_value), 10)
    text_var.set(result)


def division():
    global result
    global e
    if second_value != 0:
        result = round((first_value / second_value), 10)
        text_var.set(result)
    if second_value == 0:
        text_var.set("e")
        e = True


def addition():
    global result
    result = round((first_value + second_value), 10)
    text_var.set(result)


def subtraction():
    global result
    result = round((first_value - second_value), 10)
    text_var.set(result)


def percentage():
    global result
    if second_value != 0:
        result = (first_value / second_value * 100)
        text_var.set(result)


window = Tk()
window.title("Calculator")
window.geometry("300x350")
window.config(bg="light gray")
window.resizable(0, 0)
text_var = StringVar()
upper_frame = Frame(window, bg="light gray")
upper_frame.pack()

bottom_frame = Frame(window, bg="light gray")
bottom_frame.pack()

entry_field = Entry(upper_frame, state=NORMAL, width=16, font=("Lucida Console", 18, "bold"),
                    highlightthickness=2, textvariable=text_var)
entry_field.configure(highlightbackground="gray", highlightcolor="gray")
entry_field.pack(padx=15, pady=15)


button1 = Button(bottom_frame, text="1", width=5, height=2, font=("Verdana", 10, "bold"), command=button_1)
button1.grid(column=0, row=3, padx=5, pady=5)

button2 = Button(bottom_frame, text="2", width=5, height=2, font=("Verdana", 10, "bold"), command=button_2)
button2.grid(column=1, row=3, padx=5, pady=5)

button3 = Button(bottom_frame, text="3", width=5, height=2, font=("Verdana", 10, "bold"), command=button_3)
button3.grid(column=2, row=3, padx=5, pady=5)

button4 = Button(bottom_frame, text="4", width=5, height=2, font=("Verdana", 10, "bold"), command=button_4)
button4.grid(column=0, row=2, padx=5, pady=5)

button5 = Button(bottom_frame, text="5", width=5, height=2, font=("Verdana", 10, "bold"), command=button_5)
button5.grid(column=1, row=2, padx=5, pady=5)

button6 = Button(bottom_frame, text="6", width=5, height=2, font=("Verdana", 10, "bold"), command=button_6)
button6.grid(column=2, row=2, padx=5, pady=5)

button7 = Button(bottom_frame, text="7", width=5, height=2, font=("Verdana", 10, "bold"), command=button_7)
button7.grid(column=0, row=1, padx=5, pady=5)

button8 = Button(bottom_frame, text="8", width=5, height=2, font=("Verdana", 10, "bold"), command=button_8)
button8.grid(column=1, row=1, padx=5, pady=5)

button9 = Button(bottom_frame, text="9", width=5, height=2, font=("Verdana", 10, "bold"), command=button_9)
button9.grid(column=2, row=1, padx=5, pady=5)

button10 = Button(bottom_frame, text="0", width=5, height=2, font=("Verdana", 10, "bold"), command=button_0)
button10.grid(column=1, row=4, padx=5, pady=5)

button11 = Button(bottom_frame, text="%", width=5, height=2, font=("Verdana", 10, "bold"), command=button_percent)
button11.grid(column=0, row=0, padx=5, pady=5)

button12 = Button(bottom_frame, text="*", width=5, height=2, font=("Verdana", 10, "bold"), command=button_multiply)
button12.grid(column=3, row=1, padx=5, pady=5)

button13 = Button(bottom_frame, text="/", width=5, height=2, font=("Verdana", 10, "bold"), command=button_division)
button13.grid(column=3, row=0, padx=5, pady=5)

button14 = Button(bottom_frame, text="+", width=5, height=2, font=("Verdana", 10, "bold"), command=button_addition)
button14.grid(column=3, row=3, padx=5, pady=5)

button15 = Button(bottom_frame, text="-", width=5, height=2, font=("Verdana", 10, "bold"), command=button_distraction)
button15.grid(column=3, row=2, padx=5, pady=5)

button16 = Button(bottom_frame, text="=", width=5, height=2, font=("Verdana", 10, "bold"), command=button_equals)
button16.grid(column=3, row=4, padx=5, pady=5)

button17 = Button(bottom_frame, text="C", width=5, height=2, font=("Verdana", 10, "bold"), command=button_C)
button17.grid(column=1, row=0, padx=5, pady=5)

button18 = Button(bottom_frame, text="<--", width=5, height=2, font=("Verdana", 10, "bold"), command=button_del)
button18.grid(column=2, row=0, padx=5, pady=5)

button19 = Button(bottom_frame, text="+/-", width=5, height=2, font=("Verdana", 10, "bold"), command=button_plus_min)
button19.grid(column=0, row=4, padx=5, pady=5)

button20 = Button(bottom_frame, text=".", width=5, height=2, font=("Verdana", 10, "bold"), command=button_dot)
button20.grid(column=2, row=4, padx=5, pady=5)

window.mainloop()
