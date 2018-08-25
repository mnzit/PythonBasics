class Car:
    # class variables

    wheels = 4

    def __init__(self):

        # belongs to instance namespace

        self.mil = 10
        self.com = "BMW"

c1 = Car()

c2 = Car()

# belongs class variables

Car.wheels = 5

# namespace is an area where you create and store object/variable
# - class namespace
# - object namespace

# c1, c2 are are objects so their variables are instance variables

print(c1.com, c1.mil, c1.wheels)
print(c2.com, c2.mil, c2.wheels)