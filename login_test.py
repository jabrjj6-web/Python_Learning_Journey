print("--- Secure Login System ---")

# استقبال مدخلات المستخدم
username = input("Username: ")
password = input("Password: ")

print("--------------------------")

# التحقق من البيانات (مع تصحيح إملاء المتغيرات)
if username == "jabr" and password == "12345":
    print("Welcome back, Jabr! Login successful. 🎉")
else:
    print("Access Denied: Incorrect username or password. ❌")
