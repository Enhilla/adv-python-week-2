a = float(input("First number: "))
op = input("Operation (+, -, *, /): ")
b = float(input("Second number: "))

if op == "+":
   result = (a + b)

elif op == "-":
    result = (a - b)

elif op == "*":
    result = (a * b)

elif op == "/":
    if b:
        result = (a / b)
    else:
        result = "Error: division by zero"


print(f"{a} {op} {b} = {result}")