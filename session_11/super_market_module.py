from tkinter import *
from tkinter import messagebox


product_list = []
total = 0

# window
window = Tk()
window.title("Product List")
window.geometry("600x400")

#Id
Label(window, text="Id").place(x=20, y=20)
id = StringVar()
Entry(window, textvariable=id).place(x=100, y=20)

# Name
Label(window, text="Name").place(x=20, y=60)
name = StringVar()
Entry(window,textvariable= name).place(x=100, y=60)

#brand
Label(window, text="Brand").place(x=20, y=100)
brand = StringVar()
Entry(window,textvariable= brand).place(x=100, y=100)

# Quantity
Label(window,text="Quantity").place(x=20, y=140)
quantity = IntVar()
Entry(window,textvariable=quantity).place(x=100, y=140)



# Price
Label(window,text="Price").place(x=20, y=180)
price = IntVar()
Entry(window,textvariable=price).place(x=100, y=180)


# Expire Date
Label(window,text="ExpireDate").place(x=20, y=220)
expiredate = IntVar()
Entry(window,textvariable=expiredate).place(x=100, y=220)



window.mainloop()

