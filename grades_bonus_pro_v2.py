print("--- Student Grades Bonus System ---\n")

# قائمة الدرجات الأصلية
grades = [98, 69, 78, 88, 55, 29]
new_grades = []

# حلقة تكرار لإضافة 5 درجات بونص لكل طالب
for grade in grades:
    bonus = grade + 5
    new_grades.append(bonus)

# طباعة النتائج بشكل منظم ومكتوب صح
print("Original Grades:    ", grades)
print("Grades After Bonus: ", new_grades)
