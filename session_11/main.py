super_market = []

import re


def divide(a, b):
    return a / b


def id_validator(id):
    if not re.match(r"^[a-zA-Z\s]{3,30}$", id):
        raise ValueError("Invalid id !!!")


def name_validator(name):
    if not re.match(r"^[a-zA-Z\s]{3,30}$", name):
        raise ValueError("Invalid Name !!!")


def brand_validator(brand):
    if not re.match(r"^[a-zA-Z\s]{3,30}$", brand):
        raise ValueError("Invalid brand !!!")


def quantity_validator(quantity):
    if not (quantity == int and 0 < quantity):
        raise ValueError("Invalid quantity !!!")
