print("--- User Search System (Break Demo) ---\n")

# قائمة الأسماء مكتوبة بتهجئة صحيحة وتبدأ بحروف كبيرة
names = ["Ahmed", "Adel", "Jabr", "Hassan"]

# حلقة تكرار للبحث عن اسم محدد
for name in names:
    if name == "Jabr":
        print(f"-> Target found: [ {name} ]! Stopping the search.")
        break
    print(f"Checking: {name}")

print("\nSearch process finished.")
