print("--- Custom List Indexing Demo ---\n")

# تعريف القائمة بأسماء منسقة تبدأ بحروف كبيرة
mixed_list = ["Ahmed", 50, "Adel", 20]

# الطريقة الأولى: الوصول للعناصر يدوياً عبر الـ Index باستخدام f-string
print("Accessing Elements Manually:")
print(f"Index 0: {mixed_list[0]}")
print(f"Index 1: {mixed_list[1]}")
print(f"Index 2: {mixed_list[2]}")
print(f"Index 3: {mixed_list[3]}")

print("\n" + "-" * 35)

# الطريقة الثانية: المرور الذكي على العناصر باستخدام Loop (إضافة برمجية فخمة)
print("Iterating Elements Dynamically:")
for index, item in enumerate(mixed_list):
    print(f"Item at position {index} is -> {item}")
