

class Menu(dict):
    """fill in class definition here"""


class Order:
    """fill in class definition here"""


class Bill:
    """fill in class definition here"""


m = Menu()
m["idly"] = 20
m["vada"] = 20

o = Order(m)
try:
    o["vada"] = 2
    o["pongal"] = 2

except KeyError as e:
    print(e)

b = Bill(m, o)
print(b)
"""
# Loops & Iterators

largest = None
smallest = None

while True:
    num = input("Enter a number? ")

    if num == "done":
        break

    # ...

    print(num)

print("Maximum", largest)
"""