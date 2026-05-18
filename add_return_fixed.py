print("--- Advanced Function Demo (Return Value) ---\n")

# دالة جمع ترجع القيمة بشكل نظيف وهندسي
def add_numbers(x, y):
    return x + y

# استدعاء الدالة وتخزين النتيجة المرجعة في متغير
num1, num2 = 10, 20
result = add_numbers(num1, num2)

# طباعة المخرجات بأناقة الـ f-string
print(f"Input Values:     {num1} and {num2}")
print(f"Returned Result:  {result}")

print("\nFunction return test completed successfully!")
