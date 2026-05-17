# دالة تستقبل الاسم، العمر، والرقم التعريفي
def say_hello(name, age, user_id):
    print(f"Hello, {name}!")
    print(f"Your age is: {age}")
    print(f"Your ID is:  {user_id}")

print("--- User Profile Information ---\n")

# استدعاء الدالة وتمرير البيانات لها
say_hello("Adel", 16, 20)
