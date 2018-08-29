# Inheritance
# Single Level Inheritance

# class A:
#     def feature1(self):
#         print("Feature 1 is progress")
#
#     def feature2(self):
#         print("Feature 2 is progress")
#
#
# class B(A):
#     def feature3(self):
#         print("Feature 3 is progress")
#
#     def feature4(self):
#         print("Feature 4 is progress")
#
# b1 = B()
#
# b1.feature1()
# b1.feature2()
# b1.feature3()
# b1.feature4()

# Multi Level Inheritance

# class C:
#     def feature1(self):
#         print("Feature 1 is progress")
#
#     def feature2(self):
#         print("Feature 2 is progress")
#
#
# class D(C):
#     def feature3(self):
#         print("Feature 3 is progress")
#
#     def feature4(self):
#         print("Feature 4 is progress")
#
# class E(D):
#     def feature5(self):
#         print("Feature 5 is progress")
#
#     def feature6(self):
#         print("Feature 6 is progress")
#
#
# e1 = E()
#
# e1.feature1()
# e1.feature2()
# e1.feature3()
# e1.feature4()
# e1.feature5()
# e1.feature6()

# Multiple Inheritance

# class X:
#     def feature1(self):
#         print("Feature 1 is progress")
#
#     def feature2(self):
#         print("Feature 2 is progress")
#
# class Y:
#     def feature3(self):
#         print("Feature 3 is progress")
#
#     def feature4(self):
#         print("Feature 4 is progress")
#
# class Z(X, Y):
#     def feature5(self):
#         print("Feature 5 is progress")
#
# z1 = Z()
#
# z1.feature1()
# z1.feature2()
# z1.feature3()
# z1.feature4()
# z1.feature5()

# Constructor in inheritance
# If B doesnt have constructor defined it will call A's Constructor

# class A:
#     def __init__(self):
#         print("Print in A Init")
#
#     def feature1(self):
#         print("Feature 1 is progress")
#
#     def feature2(self):
#         print("Feature 2 is progress")
#
#
# class B(A):
#     def __init__(self):
#
#         # Accessing init of super class
#
#         super().__init__()
#         print("Print in B Init")
#
#     def feature3(self):
#         print("Feature 3 is progress")
#
#     def feature4(self):
#         print("Feature 4 is progress")
#
# b1 = B()

class A:
    def __init__(self):
        print("Print in A Init")

    def feature1(self):
        print("Feature 1 is progress")

    def feature2(self):
        print("Feature 2 is progress")

    def newFeature(self):
        print("And here is our new feature from A")

class B:
    def __init__(self):
        print("Print in B Init")

    def feature3(self):
        print("Feature 3 is progress")

    def feature4(self):
        print("Feature 4 is progress")

    def newFeature(self):
        print("And here is our new feature from B")

# Multiple Level inheritance has the feature of MRO (MEthod resoultion order)
# Left to Right
# Same Rule to Methods too

class C(A, B):
    def __init__(self):
        super().__init__()
        print("Print in C Init")

    def feat(self):
        super().feature2()

c1 = C()
c1.newFeature()

