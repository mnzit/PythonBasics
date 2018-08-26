#INNER CLASS

class Person:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.laptop = self.Laptop()

    def show(self):
        print(self.name, self.rollno)
        self.laptop.show()

    class Laptop:

        def __init__(self):
            self.brand = 'DELL'
            self.cpu = 'i5'
            self.ram = 16

        def show(self):
            print(self.ram, self.cpu, self.brand)

s1 = Person('Manjit', 2)
s2 = Person('Sandesh', 4)

s1.show()

# lap1 = s1.laptop
# lap2 = s2.laptop

lap1 = Person.Laptop()


# print(id(lap1))
# print(id(lap2))