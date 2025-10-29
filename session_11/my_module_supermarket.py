import from super_market
import re


def name_validator(name):
    if not re.match(r"^[a-zA-Z\s]{3,30}$", name):
        raise NameError("invalid name!")


def brand_validator(brand):
    if not re.match(r"^[a-zA-Z\s]{3,30}$", brand):
        raise NameError("invalid brand!")

def quantity_validator(quantity):
    if not (type(quantity) == int and quantity > 0):
        raise NameError("invalid quantity!")

def price_validator(price):
    if not (type(price) == float and price >0 ):
        raise NameError("invalid price!")

def expiration_date_validator(expiration_date):
    if not expire_date > datetime.today().date():
        raise NameError("invalid expiration date!")
