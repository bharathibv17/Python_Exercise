a = int(input("Enter the first number : "))
b = int(input("Enter the second number: "))
c = input("Enter the operation you want to perform (+,-,*,/): ")

if c == '+':
    result = a+b
elif c == '-':
    result = a-b
elif c == '*':
    result = a * b
elif c == '/':
    if b!=0:
        result = a/b
    else:
        result = "undefined(cannot be divided by zero"
else:
    result = "Invalid operation"

print("The result of : ", result)



