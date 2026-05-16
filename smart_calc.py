num1 = float(input("enter farest nombr : "))
opar = input("choose an oprint (+,-,/,*,%) : ")
num2 = float(input("your cloocand nombr : "))

print("----------------------------------\n")

if opar == "+":
    result = num1 + num2
    print(num1, "+", num2, "=", result)

elif opar == "-":
    result = num1 - num2
    print(num1, "-", num2, "=", result)

elif opar == "*":
    result = num1 * num2
    print(num1, "*", num2, "=", result)

elif opar == "/":
    result = num1 / num2
    print(num1, "/", num2, "=", result)

elif opar == "%":
    result = num1 % num2
    print(num1, "%", num2, "=", result)

else:
    print("Error")