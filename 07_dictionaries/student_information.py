student = {
    "name": "Olamide",
    "age": 25,
    "country": "Nigeria",
    "course": "Data Analysis"
}

print("Name:", student["name"])
print("Country:", student["country"])
print("Course:", student.get("course"))
print("Email:", student.get("email", "Not Available"))