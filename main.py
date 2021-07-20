from tkinter import *


TITLE = "Mile to Km Project"

screen = Tk()
screen.title(TITLE)
screen.configure(padx=50,pady=50)
user_input = Entry(width=10)
screen.minsize(width=200, height=100)
user_input.grid(column=2, row=1)
miles = Label(text="Miles")
miles.grid(column=3, row=1)
equal_to_label = Label(text="is equal to ")
equal_to_label.grid(column=0, row=2)
km_label = Label(text="Km")
km_label.grid(column=3, row=2)
button = Button(text="Calculate")
button.grid(column=2, row=3)

def formula():
    km = round(float(user_input.get()) / 0.62137)
    result = Label(text=km)
    result.grid(column=2, row=2)

button.configure(command=formula)



















screen.mainloop()
