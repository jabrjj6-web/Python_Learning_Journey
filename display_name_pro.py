# دالة ترحيبية تستقبل الاسم كمتغير
def display(username):
    return f"Welcome, {username}!"

# نطلب من المستخدم إدخال اسمه
user_input = input("Enter your name: ")

# نستدعي الدالة ونمرر لها الاسم المدخل
message = display(user_input)

# نطبع رسالة الترحيب
print(message)
