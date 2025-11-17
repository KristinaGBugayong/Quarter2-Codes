n = int(input("Enter number of students: "))
s = int(input("Enter number of subjects: "))
total = 0
count = 0

for i in range(1, n+1):
    print(f"\nStudent {i}")
    sum_stu = 0
    for j in range(1, s+1):
        score = float(input(f"Enter score {j}: "))
        sum_stu += score
        total += score
        count += 1
    avg = sum_stu / s
    print(f"Average for Student {i} = {avg:.1f}")

print(f"\nClass Average = {total/count:.1f}")
