print("--- Age in Hours Calculator ---")

# دمجنا الإدخال والتحويل في سطر واحد واحترافي
age_days = int(input("Enter your age in days: "))

# حساب الساعات
age_hours = age_days * 24

# طباعة النتيجة مع تنظيم الحروف الكبيرة في النص
print(f"You have lived for {age_hours:,} hours.")
