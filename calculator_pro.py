print("| Welcome to Calculator |\n")

# استقبال الأرقام بشكل نظيف
number1 = float(input("First number: "))
number2 = float(input("Second number: "))

print("| --------------------- |")

# طباعة العمليات باستخدام الـ f-string الاحترافية بدون تعقيد str()
print(f"Addition:       {number1 + number2}")
print(f"Subtraction:    {number1 - number2}")
print(f"Multiplication: {number1 * number2}")
print(f"Division:       {number1 / number2}")
print(f"Modulus:        {number1 % number2}")
