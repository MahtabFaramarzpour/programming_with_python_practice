from tkinter import *
from tkinter import messagebox
from my_module_supermarket import *
from datetime import datetime,date
from tkinter import ttk

from session_11.main import id_validator

product_list = []

def save():
    try:
        # todo run (2 ta window baz mishe)
        # todo name_validator
        # todo line 18
        id_validator(id.get())
        name_validator(name.get())
        brand_validator(brand.get())
        price_validator(price.get())
        quantity_validator(quantity.get())
        table.insert("", END,values=tuple(product.values()))


        expire_date = datetime.strptime(expiration_date.get(), "%Y-%m-%d").date()
        expiration_date_validator(expire_date)

        product = {
            "id": id.get(),
            "name": name.get(),
            "brand": brand.get(),
            "quantity": quantity.get(),
            "price": price.get(),
            "expire_date": expiration_date.date()
        }
        product_list.append(product)
        messagebox.showinfo("Saved",  "Product Saved Successfully")
        id.set(0)
        name.set("")
        brand.set("")
        quantity.set(0)
        price.set(0.0)
        expire_date.set(str(date.today()))
    except Exception as e:
        messagebox.showerror("Save Error", f"Error: {e}")

def total_price():
    try:
        total = calculate_total(product_list)
        messagebox.showinfo("Total Price", f"Total value of all products: {total}\n {to_word(total)} تومان")
    except Exception as e:
        messagebox.showinfo("Error", "No Products Available")
        return

    total = 0
    for product in product_list:
        total += product["quantity"] * product["price"]

window = Tk()
window.title("Super Market")
window.geometry("800x600")
window.config(background = "misty rose")

# ID
Label (window, text="Id:").place(x=40, y=40)
Id = IntVar()
Entry(window, textvariable=id, state="readonly").place(x=160, y=40)

# Name
Label (window, text="Name:").place(x=40, y=80)
name = StringVar()
Entry(window, textvariable=name).place(x=160, y=80)

# Brand
Label(window, text="Brand:").place(x=40, y=120)
brand = StringVar()
Entry(window, textvariable=brand).place(x=160, y=120)

# Quantity
Label(window, text="Quantity:").place(x=40, y=160)
quantity = IntVar()
Entry(window, textvariable=quantity).place(x=160, y=160)

# Price
Label(window, text="Price:").place(x=40, y=200)
price = DoubleVar()
Entry(window, textvariable=price).place(x=160, y=200)

# Date
Label(window, text="Expiration date\n YYYY-MM-DD").place(x=40, y=240)
exp_date = StringVar()
Entry(window, textvariable=exp_date).place(x=160, y=240)

Button(window, text="Save", command=save).place(x=150, y=280, width=140)
Button(window, text="Total", command=total_price).place(x=150, y=320, width=140)



table = ttk.Treeview(window, columns=[1, 2, 3, 4, 5, 6], height= 14, show="headings")

table.heading("1", text="ID")
table.heading("2", text="Name")
table.heading("3", text="Brand")
table.heading("4", text="Quantity")
table.heading("5", text="Price")
table.heading("6", text="Expiration date")


table.column(1, width=40)
table.column(2, width=100)
table.column(3, width=100)
table.column(4, width=60)
table.column(5, width=60)
table.column(6, width=100)





table.place(x=300, y=40)
window.mainloop()













