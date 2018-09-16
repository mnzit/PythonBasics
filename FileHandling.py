# f = open('MyData', 'r')


# read data
# print(f.readline(), end="#")


# Write
# f1 = open('abc', 'w')
# # f1.write("Something")
# f1.write("Peoplee")

# append
# f1 = open('abc', 'a')
# f1.write("Manjit")


# for data in f:
#     print(data)\


# for data in f:
#     f1.write(data)

f = open('dead.jpg', 'rb')

# for i in f:
#     print(i)

f1 = open('myPic.jpg', 'wb')

for i in f:
    f1.write(i)


