a = 5
b = 4

try:
    print("Resource OPEN")
    print(a/b)
    k = int(input("Enter a number"))
    print(k)
except ZeroDivisionError as e:
    print("Hey you cannot divide a Number by Zero: ", e)
except ValueError as e:
    print("You must enter a number: ", e)
except Exception as e:
    print("Something went wrong ", e)
finally:
    print("Resource CLOSE")