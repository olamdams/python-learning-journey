age = int(input("Enter your age: "))
has_drivers_id = input("Do you have a driver's license? (yes/no): ").lower() == "yes"

if age >= 18:
    if has_drivers_id:
        print("You are allowed to drive.")
    else:
        print("You are old enough, but you need a driver's license.")
else:
    print("You are too young to drive.")