student = {
    "name": "Olamide",
    "age": 25,
    "course": "Data Analysis",
    "country": "Nigeria"
}

print("Keys:")
print(student.keys())

print("\nValues:")
print(student.values())

print("\nItems:")
print(student.items())

print("\nCountry:")
print(student.get("country"))

student.update({"age": 26})

print("\nUpdated Record:")
print(student)