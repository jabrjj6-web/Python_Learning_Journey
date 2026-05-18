print("--- Advanced Function Multi-Call Demo ---\n")

# بناء دالة الجمع باستخدام return القياسي
def add_numbers(x, y):
    return x + y

# الاستدعاء الأول للدالة
res1 = add_numbers(4, 4)
print(f"Call 1 -> Operation: 4 + 4  | Result: {res1}")

# الاستدعاء الثاني للدالة
res2 = add_numbers(10, 15)
print(f"Call 2 -> Operation: 10 + 15 | Result: {res2}")

print("\nMulti-call function testing passed successfully!")
