# Find out address or id

# a = 9
# print(id(a))
# ------------------------------------------------------------------------------------------------------------
# find out type

# str = "manjit"
# print(type(str))
# --------------------------------------------------------------------------------------------------------------
# range

# print(set(range(10)))
# --------------------------------------------------------------------------------------------------------------
# key value pairs---Dictionary-Mapping

# d = {'Manjit':'Huawei','Sandesh':'Samsung'}
# print(d)
# print(d.keys())
# print(d.values())
# print(d.get('Sandesh'))
# --------------------------------------------------------------------------------------------------------------
# list slower in comparision to tuple as it is changeble

# nums = [23,12,33,55,32,123,53]
# print(nums[4])
# print(nums[2:])
# --------------------------------------------------------------------------------------------------------------
# Dont want to change the value, so iteration is faster || tuple is immutable

# tup = (21,43,56,6,2)
# print(tup[1])
# --------------------------------------------------------------------------------------------------------------
# Sets collection of unique elements--> Doesnt follows the sequences

# s={21,43,43,34}
# print(s)
# s.pop()
# print(s)
# s.push(99)
# print(s)
# --------------------------------------------------------------------------------------------------------------
# getting value from user------------------------>

# x = int(input("Enter 1st number"))
# y = int(input("Enter 2nd number"))
# z = x+y
# print(z)
# --------------------------------------------------------------------------------------------------------------
# getting char----------------------------------->

# ch = input('Enter a Char')[1]
# print(ch)
# --------------------------------------------------------------------------------------------------------------
# using expression------------------------------->

# result = eval(input('enter an expression'))
# print(result)
# --------------------------------------------------------------------------------------------------------------
# cmd value pass--------------------------------->

# import sys
# x = sys.argv[1]
# --------------------------------------------------------------------------------------------------------------
# cube------------------->

# x = int(input("Enter a number"))
# y = x**x
# print(y)
# --------------------------------------------------------------------------------------------------------------
# if condition------------------>
# x = int(input())
# r = x % 2
# if r == 0:
#     print("Even")
# else:
#     print("Odd")
# --------------------------------------------------------------------------------------------------------------
# If condition example
# x = int(input())
# if (x == 1):
#     print("One")
#
# elif (x == 2):
#     print("Two")
#
# elif (x == 3):
#     print("Three")
#
# elif (x == 4):
#     print("Four")
# else:
#     print("Wrong Input!!")

# if condition task------------------------>
# x = int(input("Enter first number: "))
# y = int(input("Enter second number: "))
# z = int(input("Enter third number: "))
#
# if(x>y and x>z):
#     print('The greatest is: ',x)
# elif(y>x and y>z):
#     print('The greatest is: ',y)
# else:
#     print('The greatest is: ',z)
# --------------------------------------------------------------------------------------------------------------
# <-------------LOOPS--------------------->

# <------------WHILE LOOPS------------------------------->
# i = 1
# while i <=5:
#     print("Manjit ",end="")
#     j = 1
#     while j <= 4:
#         print("Shakya ",end="")
#         j = j + 1
#     i = i+1
#     print()
# ---------------------------------Ending the code
# --------------------FOR LOOPS

# x = ['Manjit',2,7,8]
# x = 'MANJIT'

# for i in [2,3,5]:
#     print(i)

# for i in range(2,11,2):
#     print(i)

# --reverse--
# for i in range(20,1,-1):
# print(i)

# for i in range(1,21):
#     if i % 5 != 0:
#         print(i)

# for i in range(1,101):
#     if i % 3 != 0 and i % 5 != 0:
#         print(i)

# Break || continue || pass

# Break

# av = 10
# x = int(input("How many Candies you want?: "))
#
# i = 1
# while i <= x:
#     if i > av:
#         print("Out of Stock")
#         break
#     print("Candy:",i)
#     i+=1
#
# print("Bye")

# continue

# for i in range(1,101):
#     if i % 3 == 0 or i % 5 == 0:
#         continue
#     print(i)
# print("Bye!")

# pass
#
# for i in range(1,101):
#     if i % 2 != 0:
#         pass
#     else:
#         print(i)
# print("Bye")

# Patterns

# for i in range(4):
#     print("# ", end="")
#     for j in range(3):
#         print(" # ", end="")
#     print()

# for i in range(4):
#     for j in range(i+1):
#         print(" # ", end="")
#     print()

# for i in range(4):
#     for j in range(4-i):
#         print(" # ", end="")
#     print()

# b----signed char----int
# B----unsigned char----int
# h----signed short----int
# H----unsigned short----int
# i----signed int----int
# I----unsigned int----int
# l----signed long----int
# L----unsigned long----int
# f----float---float
# d----double----double
# u----unicode-----character

# vals = arr.array('i', [5,6,7,8,9])
# print(vals)
# print(vals.buffer_info()) #size
# print(vals.reverse())
# print(vals)

# print(vals[0])

# for i in range(5):
# print(vals[i])

# for i in range(len(vals)):
#     print(vals[i])

# for e in vals:
#     print(e)

# newArray = arr.array(vals.typecode, (a*a for a in vals))

# for e in newArray:
#     print(e)

# i = 0
# while i < len(newArray):
#     print(newArr[i])
#     i+=1
# l=[]
# for i in range(10):
#     l[i]=(int(input("Enter a number ")))
# for i in range(len(l)):
#     for j in range(i + 1, len(l)):
#         if l[i] > l[j]:
#            l[i], l[j] = l[j], l[i]
#
# print(l)

# bubble sort
# import array as a
# l = []
# for i in range(5):
#     l.append(int(input("Enter a number: ")))
# for i in range(len(l)):
#     for j in range(i + 1, len(l)):
#         if l[i] > l[j]:
#             l[i], l[j] = l[j], l[i]
# print(l)

# fact = 1
# val = int(input("Enter a number: "))
# for s in range(1, val+1):
#     fact = fact*s
# print("The factorial of", val, "is:", fact)

# insert value in array
from array import *
#
# arr = array('i', [])
#
# n = int(input("Enter the length of array: "))
#
# for i in range(n):
#     arr.append(int(input("Enter the next value")))
# print(arr)
#
# # finding value inside array
# k = 0
# f = int(input("Enter number to find: "))
#
# for e in arr:
#     if e == f:
#         print(k)
#         break
#     k += 1

# ---------Deleting a particualr number from array withour inbuit functions
# from array import *
#
# arr = array('i', [])
#
# for i in range(5):
#     arr.append(int(input("Enter next number: ")))
#
# i = int(input("Enter index of number you want to delete? "))
# for j in range(i, len(arr)-1):
#     arr[j] = arr[j+1]
#
# newArray = array('i', [])
# for k in range(0, len(arr)-1):
#     newArray.append(arr[k])
# print("After deleting")
# for e in newArray:
#     print(e)

# reverse an array in python

# from array import *
#
# arr = array('i', [])
# for i in range(5):
#     i = int(input("Enter next number: "))
#     arr.append(i)
# left = 0
# right = len(arr)-1
# while left < right:
#     temp = arr[left]
#     arr[left] = arr[right]
#     arr[right] = temp
#
#     left += 1
#     right -= 1
# print(arr)

# Using  numpy

# from numpy import *

# arr = array([1, 2, 3, 4, 5], float)
# arr = linspace(0,16,10)
#     start end parts
# arr = arange(1, 15, 2)
# arr = logspace(1, 40, 5)
# arr = zeros(5)
# arr = ones(5,int)
# print(arr.dtype)
# print(arr)

# from numpy import *

# arr = array([1, 2, 4, 5, 6])
# arr = arr + 5
# print(arr)

# arr1 = array([23, 231, 122, 22])
# arr2 = array([23, 111, 233, 22])

# arr3 = arr1 + arr2
# print(sin(arr1))
# print(cos(arr1))
# print(log(arr1))
# print(sqrt(arr1))
# print(sum(arr1))
# print(min(arr1))
# print(max(arr1))
# print(sort(arr1))
# print(concatenate([arr1,arr2]))

# copying
# aliasing
# shalow copy linked with each other
# deep copy not linked
# arr1 = array([23, 11, 224, 12, 111])
# arr2 = arr1 #same memory location
# arr2 = arr1.view() #shallow copy
# arr2 = arr1.copy() #deepcopy
# arr1[1] = 22
# print(arr1)
# print(arr2)
# print(id(arr1))
# print(id(arr2))

# from numpy import *
#
# # arr1 = array([
# #                 [1, 2, 3, 2, 3, 23],
# #                 [4, 5, 6, 23, 111, 222]
# #             ])
# # # print(arr1.ndim)
# # print(arr1.size)
# # print(arr1.shape)
# # arr2 = arr1.flatten()
# # print(arr2)
# # arr3 = arr2.reshape(2,2,3)
# # print(arr3)
#
# m = matrix('1 2 3; 6 4 5; 1 2 3 ')
# m2 = matrix('2 32 2; 22 11 22; 1 2 3')
# # print(diagonal(m))
# print(m.min())
# print(m.max())
# m3 = m * m2
# print(m3)

# -------------------------------Functions in python----------------------------------------------------------->

# def greet():
#     print("Hello")
#     print("Good Morning !!")
#
# def add(a, b):
#     c = a + b
#     print(c)
# add(10,5)
#
# def sub(a, b):
#     c = a - b
#     return c
# result = sub(10, 5)
# print(result)
#
# def add_sub(x,y):
#     c = x + y
#     d = x - y
#     return c, d
#
# result1, result2 = add_sub(10,5)
# print(result1,result2)
# #immutable
# def update(x):
#     print(id(x))
#     x = 8
#     print(id(x))
#     print("Inside Function", x)
#
# a = 10
# print(id(a))
#
# update(a)
# print("Outside Function", a)

#mutable

# def update(lst):
#     print(id(lst))
#     lst[1] = 25
#     print(id(lst))
#     print("x",lst)
# lst = [100, 22, 31]
# print(id(lst))
# update(lst)
# print("lst ", lst)

# ---------------------------------------------------------------------Types of arguments

# def person(name, age):
#     print(name)
#     print(age)
# person(age=20,name='Manjit')
#
# def person(name, age=18):
#     print(name)
#     print(age)
# person(name='Melina')

# def sum(a, *b):
#     print(a)
#     print(b)
#     c = a
#     for i in b:
#         c = c + i
#     print(c)
# sum(5,6,34,78)

# ------------------------------------------------------------------- keyword variable in arguments

# def person(name, **data):
#     print(name)
#     print(data)
#     for i, j in data.items():
#         print(i,':', j)
# person('Manjit', address='Bholdhoka', age=28, mob=9808546858)

# a = 10
#
# def something():
#     global a
#     a = 15
#     print("In function ", a)
# something()
# print("Out function ", a)

# -----------------------both global and local
#
# a = 10
#
# print(id(a))
#
# def something():
#     a = 9
#     print(id(x))
#     print("In function ", a)
#     globals()['a'] = 15
# something()
#
# print("Out function ", a)

# --------------------pass list to function
# def evenOdd(*lst):
#     odd = []
#     even = []
#     for e in lst:
#         if e % 2 == 0:
#             even.append(e)
#         else:
#             odd.append(e)
#     return odd,even
#
# odd, even = evenOdd(1,2, 3, 4, 5, 6, 7, 8, 9, 10)
# print("Even : {} and Odd : {}".format(even,odd))

# def fact(n):
#     f = 1
#     for i in range(1, n+1):
#         f = f * i
#     return f
# x = 5
# result = fact(x)
# print(result)

# -----------------------Recursion in python
# import sys
# print(sys.getrecursionlimit())
# sys.setrecursionlimit(2000)
# i = 0
# def greet():
#     global i
#     i = i+1
#     print("Hello", i)
#     greet()
#
# greet()

# -------------------------factorial using recursion

# def fact(n):
#     if n == 0:
#         return 1
#     return n * fact(n - 1)
#
# result = fact(5)
# print(result)

# --------------------------Anonomous function
# f = lambda a : a * a
# result = f(5)
# print(result)
#
# f = lambda a, b : a + b
# result = f(5,5)
# print(result)


# -----------filter map reduce
#
# from functools import reduce
# def is_even(n):
#     return n % 2 == 0
# nums = [1,2,3,4,5,6]
# evens = list(filter(lambda n : n % 2 == 0, nums))

# doubles = list(map(lambda n : n * 2, evens))
# sum = reduce(lambda a, b : a + b, doubles)
# print(sum)

# --------------------Using modules
# from Calc import *
# result = mul(6, 8)
# print(result)

# def main():
#     print("myCode file")
#
# if __name__ == '__main__':
#     main()
# check second file calc

# to skip the block use pass
# use continue to skip particular part
# use break to jump out of the loo[
