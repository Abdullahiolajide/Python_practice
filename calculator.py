num1 = float(input("First number: "))
op = input("Enter operarion: ")
num2 = float(input("Second Number: "))
result = 0
if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "/":
    result = num1 / num2
else:
    result = "Invalid Operator"

print(result)