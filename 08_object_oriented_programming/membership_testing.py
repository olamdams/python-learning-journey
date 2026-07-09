students = {"Olamide", "Grace", "David"}

print("Grace" in students)
print("John" in students)


#removing duplicate
scores = [85, 90, 75, 85, 100, 90, 75]

unique_scores = list(set(scores))

print("Original Scores:")
print(scores)

print("\nUnique Scores:")
print(unique_scores)


#finding missing items
registered = {"Olamide", "Grace", "David", "Aisha"}

present = {"Olamide", "Grace"}

absent = registered - present

print("Absent Students:")
print(absent)