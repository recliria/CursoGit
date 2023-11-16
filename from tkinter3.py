import tkinter
from tkinter import *

# create window
window = Tk()
window.title("Product Sales Calculator")
window.geometry("400x400")
 
# menu
menuBar = Menu(window)
 
# create menu: File
fileMenu = Menu(menuBar, tearoff=0) #tearoff=0 removes line that separates menu from rest of program
menuBar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Open...")
fileMenu.add_command(label="Save as...")
fileMenu.add_separator()
fileMenu.add_command(label="Exit")
 
# create menu: Edit
editMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Cut")
editMenu.add_command(label="Copy")
editMenu.add_command(label="Paste")
 
# add menu to the window
window.config(menu=menuBar)
 
# Create label and input fields for user to enter product details
productLabel = Label(window, text="Product Name: ").grid(row=0, column=0)
productInputField = Entry(window).grid(row=0, column=1)
priceLabel = Label(window, text="Price per unit: ").grid(row=1, column=0)
priceInputField = Entry(window).grid(row=1, column=1)
quantityLabel = Label(window, text="Quantity: ").grid(row=2, column=0)
quantityInputField = Entry(window).grid(row=2, column=1)
totalSalesLabel = Label(window, text="Total sales: ").grid(row=3, column=0)
totalSalesInputField = Entry(window).grid(row=3, column=1)

# Calculate Button
def calculate():
 total = float(priceInputField.get()) * int(quantityInputField.get())
 totalSalesInputField.insert(END, total)

calculateButton = Button(window, text="Calculate", command=calculate).grid(row=4,column=1)
 
# run mainloop
window.mainloop()