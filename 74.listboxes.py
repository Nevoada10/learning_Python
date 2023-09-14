# listbox = A listing of selectable text items within it's own container

from tkinter import *


def submit():
    print("You ordered:")
    print(listbox.get(listbox.curselection()))  # Using the current selection.


def add():
    listbox.#(entry_box.get())


window = Tk()

# Defining the widgets of the window.

listbox = Listbox(window,
                  font=("Constancia", 35),
                  width=12,
                  fg="Black",
                  bg="Grey")

listbox.insert(1, "Pizza")
listbox.insert(2, "Pasta")
listbox.insert(3, "Garlic Bread")
listbox.insert(4, "Soup")
listbox.insert(5, "Salad")
listbox.config(height=listbox.size())

submit_button = Button(window,
                       text="Submit",
                       command=submit,
                       )

add_button = Button(window,
                    text="Add",
                    command=add
                    )

entry_box = Entry(window)

# Displaying the window with all of your widgets

entry_box.pack()
listbox.pack()  # Or place.
submit_button.pack()
window.mainloop()
