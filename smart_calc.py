print("--- Professional Python Calculator ---\n")

# استقبال المدخلات بأسماء متغيرات نظيفة ونصوص إنجليزية صحيحة
num1 = float(input("Enter first number: "))
operator = input("Choose an operator (+, -, *, /, %): ")
num2 = float(input("Enter second number: "))

print("-" * 40)

# التحقق من العمليات الحسابية وطباعة الناتج بتنسيق احترافي
if operator == "+":
    result = num1 + num2
    print(f"Result: {num1} + {num2} = {result}")

elif operator == "-":
    result = num1 - num2
    print(f"Result: {num1} - {num2} = {result}")

elif operator == "*":
    result = num1 * num2
    print(f"Result: {num1} * {num2} = {result}")

elif operator == "/":
    # حماية الكود من خطأ القسمة على صفر
    if num2 == 0:
        print("Error: Division by zero is not allowed!")
    else:
        result = num1 / num2
        print(f"Result: {num1} / {num2} = {result}")

elif operator == "%":
    if num2 == 0:
        print("Error: Cannot calculate remainder with zero!")
    else:
        result = num1 % num2
        print(f"Result: {num1} % {num2} = {result}")

else:
    print("Invalid operator! Please run the program again.")
