print("--- Custom Functions Demo (Addition) ---\n")

# بناء دالة الجمع الاحترافية باستخدام return
def add_numbers(x, y):
    return x + y

# استدعاء الدالة وتخزين النتيجة في متغير
num1, num2 = 4, 7
result = add_numbers(num1, num2)

# طباعة العملية والناتج بتنسيق f-string مودرن
print(f"Mathematical Operation: {num1} + {num2}")
print(f"Calculated Result:      {result}")

print("\nFunction executed successfully!")
