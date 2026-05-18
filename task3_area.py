print("--- Interactive User Profile Input ---\n")

# استقبال مدخلات المستخدم بنصوص إنجليزية صحيحة وتعديل اسم متغير المعدل
name = input("Enter your name: ")
age  = input("Enter your age:  ")
gpa  = input("Enter your GPA:  ")

print("\n" + "=" * 30)
print("       STUDENT CARD")
print("=" * 30)

# طباعة المخرجات بأسلوب f-string الاحترافي والمحاذاة الموزونة
print(f"Name: {name}")
print(f"Age:  {age} years old")
print(f"GPA:  {gpa}")

print("=" * 30)
