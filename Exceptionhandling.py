x = input("Enter first number")
y = input("Enter second number")
try:
    z = x / int(y)
except ZeroDivisionError as e:
    print("ZeroDivisionError exception")
except TypeError as f:
    print("TypeError exception")