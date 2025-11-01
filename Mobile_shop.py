# define function
from session_11.super_market_module import product_list


def correct_product(product):
    product["price"] = int(product["price"])
    product["name"] = product["name"].capitalize()
    product["total"] = product["quantity"] * product["price"]
    print(f"{product["name"]:10}) {product["total"]:10}")
    return product

def total_product(product):
    return product["total"]

def upper_5000(product):
    return poduct["total"] > 5000

def lower_5000(product):
    return product["total"] <= 5000

# dataset
product_list = [
    {"id": 1, "name": "mobile", "quantity": 5, "price": "400"},
     "id": 2, "name": "laptop", "quantity": 5, "price": "800"},
     "id": 3, "name": "SPEAKER", "quantity": 11, "price": "700"}
     "id": 4, "name": "mOnitor", "quantity": 3, "price": "600"}
     "id": 5, "name": "mouse", "quantity": 6, "price": "350"}
     "id": 6, "name": "keyboard", "quantity": 4, "price": "200"}
     "id": 7, "name": "toUCH", "quantity": 9, "price": "800"}
    ]

# Functional programming
product_list = list(map(correct_product, product_list))
total_list = list(map(total_product, product_list))
upper_5000_list = list(filter(upper_5000, product_list))
lower_5000_list = list(filter(lower_5000, product_list))


# Print results
print("-"*50)
print(f"Total: \t\t\t{sum(total_list)}")
print("-"*50)
print("Upper")
print(upper_5000_list)
print("-"*50)
print("Lower")
print(lower_5000_list)