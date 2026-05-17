# دالة الجمع
def add(x, y):
    return x + y

# دالة الطرح
def sub(x, y):
    return x - y

# دالة الضرب
def mul(x, y):
    return x * y

# دالة القسمة مع حماية الكود من القسمة على صفر
def div(x, y):
    if y == 0:
        return "Error (Division by zero)"
    return x / y

print("--- Multi-Function Calculator Demo ---\n")

# تحديد الأرقام للتجربة
num1 = 20
num2 = 5

# طباعة العمليات بشكل منظم ومحاذاة مثالية
print(f"Numbers used:    {num1} and {num2}\n")
print(f"Addition:       {num1} + {num2} = {add(num1, num2)}")
print(f"Subtraction:    {num1} - {num2} = {sub(num1, num2)}")
print(f"Multiplication: {num1} * {num2} = {mul(num1, num2)}")
print(f"Division:       {num1} / {num2} = {div(num1, num2)}")
