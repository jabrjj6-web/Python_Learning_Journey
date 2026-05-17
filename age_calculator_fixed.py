print("--- Age Calculator Pro ---")

age_years = int(input("Enter your age in years: "))

# العمليات الحسابية
age_months = age_years * 12
age_days = age_years * 365
age_hours = age_days * 24

# طباعة النتائج بشكل منظم
print(f"You have lived for:")
print(f"- {age_months} Months")
print(f"- {age_days} Days")
print(f"- {age_hours} Hours")
