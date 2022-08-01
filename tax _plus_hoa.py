from tkinter import *
from tkinter import messagebox
import locale
import sys


def calculate():
    if value.get() == "" and hoa.get() == "":
        messagebox.showwarning("Warning", "Please fill out the Property value and Monthly HOA fields.")

    elif value.get() == "" and hoa.get().isnumeric():
        messagebox.showwarning("Warning", "Please fill out the Property value field.")

    elif hoa.get() == "" and value.get().isnumeric():
        messagebox.showwarning("Warning", "Please fill out Monthly HOA field.")
    elif not value.get().isnumeric() and hoa.get().isnumeric():
        messagebox.showerror("Error", "Please enter numeric value for Property value field.")
        value_entry.delete(0, END)
    elif not value.get().isnumeric() and hoa.get() == "":
        messagebox.showerror("Error", "Please enter numeric value for Property value "
                                      "field and fill out Monthly HOA field.")
        value_entry.delete(0, END)
    elif not hoa.get().isnumeric() and value.get().isnumeric():
        messagebox.showerror("Error", "Please enter numeric value for Monthly HOA field.")
        hoa_entry.delete(0, END)
    elif not hoa.get().isnumeric() and value.get() == "":
        messagebox.showerror("Error", "Please enter numeric value for Monthly HOA "
                                      "field and fill out Property value field.")
        hoa_entry.delete(0, END)
    elif not hoa.get().isnumeric() and not value.get().isnumeric():
        messagebox.showerror("Error", "Please enter numeric values for Monthly HOA and Property value fields.")
        hoa_entry.delete(0, END)
        value_entry.delete(0, END)

    elif value.get().isnumeric and hoa.get().isnumeric():
        property_value = float(value.get())
        assessment_value = property_value * 0.6
        hoa_value = float(hoa.get())
        hoa_total = hoa_value * 12
        property_tax_total = assessment_value / 100 * 0.75 * 12
        grand_total = hoa_total + property_tax_total

        locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
        assessment_value = locale.currency(assessment_value, grouping=True)
        grand_total = locale.currency(grand_total, grouping=True)
        messagebox.showinfo("Calculation results", "Assessment Value of Property is " + str(
            assessment_value) + "\n" + "Total Property Tax Bill Amount is " + str(grand_total))


def clear():
    value_entry.delete(0, END)
    hoa_entry.delete(0, END)


window = Tk()
window.title("Property Tax Bill")
window.geometry("500x260")
window.configure(bg="light blue")
window.resizable(False, False)

value = StringVar()
hoa = StringVar()

upper_frame = Frame(window, bg="light green", bd=1, relief=SUNKEN)
upper_frame.grid(row=0, column=0, pady=20, padx=20)

bottom_frame = Frame(window, bg="light blue")
bottom_frame.grid(row=1, column=0, pady=10)

value_label = Label(upper_frame, bg="light green", font=("Arial", 14), fg="dark blue", text="Enter property value")
value_label.grid(row=0, column=0, padx=20, pady=20, sticky=W)

value_entry = Entry(upper_frame, textvariable=value, font=("Unispace", 12, "bold"))
value_entry.grid(row=0, column=1, padx=20, pady=20)

hoa_label = Label(upper_frame, bg="light green", font=("Arial", 14), fg="dark blue", text="Enter monthly HOA")
hoa_label.grid(row=1, column=0, padx=20, pady=20, sticky=W)

hoa_entry = Entry(upper_frame, textvariable=hoa, font=("Unispace", 12, "bold"))
hoa_entry.grid(row=1, column=1, padx=20, pady=20)

button_calculate = Button(bottom_frame, font=("Unispace", 10, "bold"), fg="dark green", bg="dark gray",
                          text="  Calculate  ", command=calculate)
button_calculate.grid(row=0, column=0, padx=15, pady=10)

button_clear = Button(bottom_frame, font=("Unispace", 10, "bold"), fg="dark green", bg="dark gray",
                      text="    Clear    ", command=clear)
button_clear.grid(row=0, column=1, padx=15, pady=10)

button_exit = Button(bottom_frame, font=("Unispace", 10, "bold"), fg="dark green", bg="dark gray", text="    Exit    ",
                     command=sys.exit)
button_exit.grid(row=0, column=2, padx=15, pady=10)

window.mainloop()
