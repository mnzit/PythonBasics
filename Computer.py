class Computer:
    cpu = ''
    ram = ''

    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("Config is ", self.cpu, self.ram)


com1 = Computer('i5', '16GB')
com2 = Computer('i7', '8GB')

# Computer.config(com1)
# Computer.config(com2)

com1.config()
com2.config()

# print(type(com))

