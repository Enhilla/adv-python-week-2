a = float(input("First number: "))
op = input("Operation (+, -, *, /): ")
b = float(input("Second number: "))

if op == "+":
    result = a + b
elif op == "-":
    result = a - b
elif op == "*":
    result = a * b
elif op == "/":
    if b != 0:
        result = a / b
    else:
        print("Error: division by zero")
        exit()
else:
    print("Unknown operation")
    exit()

print(f"{a} {op} {b} = {result}")
