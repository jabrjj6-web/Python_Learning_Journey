print("--- Numbers from 1 to 10 (Skipping 6) ---\n")

for i in range(1, 11):
    if i == 6:
        # تخطي الرقم 6 دون طباعته
        continue
    
    print(f"Number: {i}")
