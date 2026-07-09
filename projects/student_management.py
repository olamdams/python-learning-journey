student = {
    "name": "Olamide",
    "age": 40,
    "course": "Data Science"
}

# Add a new key
student["grade"] = "A"

# Update the age
student["age"] = 41

# Remove the course key
student.pop("course")

# Display the remaining information
for key, value in student.items():
    print(f"{key}: {value}")