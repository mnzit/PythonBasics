# DuckTyping
# If it quacks like a duck, Swims like a duck, Walks like a duck then its a Duck


# class PyCharm:
#
#     def execute(self):
#         print("Compiling")
#         print("Running")
#
# class NetBeans:
#
#     def execute(self):
#         print("Spell Check")
#         print("Compiling")
#         print("Running")
#
# class Laptop:
#
#     def code(self, ide):
#         ide.execute()
#
# ide = NetBeans()
#
# lap1 = Laptop()
#
# lap1.code(ide)

# Operator overloading


# For clearance

# a = 5
# b = 'World'

# Predefined Synthetic Sugar
# print(a+b)

# print(int.__add__(a,b))

#magic methods
# __add__()
# __sub__()
# __mul__()
#
# class Student:
#
#     def __init__(self, m1,  m2):
#         self.m1 = m1
#         self.m2 = m2
#
#     def __add__(self, other):
#         m1 = self.m1 + other.m1
#         m2 = self.m2 + other.m2
#         s3 = Student(m1, m2)
#         return s3
#
#     def __gt__(self, other):
#         r1 = self.m1 + self.m2
#         r2 = other.m1 + other.m2
#         if r1 > r2:
#             return True
#         else:
#             return False
#
#     def __str__(self):
#         return '{} {}'.format(self.m1, self.m2)
#
#     def __mod__(self, other):
#         m1 = self.m1 + self.m2
#         m2 = other.m1 + other.m2
#         return m1 % m2
#
# s1 = Student(20, 69)
# s2 = Student(20, 33)
#
# s3 = s1 + s2
#
# print(s3.m1)
#
# if s1 > s2:
#     print("S1 wins")
# else:
#     print("S2 wins")
#
# print(s1)
#
# print(s1 % s2)


# method overloading and method overriding

# Method overloading not available in python


# class Student:
#     def __init__(self):
#         print('This is the Student')
#
#     def sum(self, a = None, b = None, c = None):
#         s = 0
#         if a != None and b != None and c != None:
#             s =a+b+c
#         elif a != None and b != None:
#             s = a+b
#         else:
#             s = a
#         return s
#
# s1 = Student()
# print (s1.sum(12))


class A:
    def show(self):
        print("in A Show")

class B(A):
    def show(self):
        print("in B Show")


a1 = B()

a1.show()