age = int(input("Enter your age: "))
has_id = input("Do you have an ID? (yes/no): ").lower()

if age >= 18 and has_id == "yes":
    print("You may enter.")
else:
    print("You cannot enter.")