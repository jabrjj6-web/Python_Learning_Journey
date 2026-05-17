print("--- List Element Deletion Demo ---\n")

# قائمة الفواكه مكتوبة بتهجئة صحيحة
fruits = ["apple", "banana", "orange"]

# طباعة القائمة قبل الحذف باستخدام f-string
print(f"Original List: {fruits}")

# حذف العنصر الثالث (Index 2) وهو orange
del fruits[2]

# طباعة القائمة بعد التعديل
print(f"Updated List:  {fruits}")
