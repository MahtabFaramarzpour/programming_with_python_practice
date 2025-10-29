from tkinter import *
from tkinter import messagebox
from my_module import *
from datetime import datetime,date



product_list = []

def save():
    try:
        name_validator(name.get())
        brand_validator(brand.get())
        quantity_validator(quantity.get())
        price_validator(price.get())
        exp_date = datetime.strptime(expire_date.get(), "%Y-%m-%d").date()
        expiration_date_validator(exp_date)

        product = {
            "id": id.get(),
            "name": name.get(),
            "brand": brand.get(),
            "quantity": quantity.get(),
            "price": price.get(),
            "expiration_date": exp_date
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
    if not product_list:
        messagebox.showerror("No Products", "No Products Available")
        return

    total = 0
    for product in product_list:
        total += product["quantity"] * product["price"]

window = Tk()
window.title("Super Market")
window.geometry("800x600")


# ID
Label (window, text="ID).place(x=40, y=40)")
id = IntVar()
Entry(window, textvariable=id).place(x=160, y=40)

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
quantity = StringVar()
Entry(window, textvariable=quantity).place(x=160, y=160)

# Price
Label(window, text="Price:").place(x=40, y=200)
price = DoubleVar()
Entry(window, textvariable=price).place(x=160, y=200)

# Date
Label(window, text="Expiration date\n YYYY-MM-DD").place(x=40, y=240)
exp_date = StringVar()
Entry(window, textvariable=exp_date).place(x=160, y=240)

Button (window, text="Save", command=save).place(x=160, y=280, width=300)
Button (window, text="Total", command=total_price).place(x=160, y=280, width=300)



window.mainloop()













