age = int(input("Enter your age: "))

if age >= 18:

    has_laptop = input("Do you have a laptop? (yes/no): ").lower() == "yes"

    if has_laptop:

        has_internet = input("Do you have internet access? (yes/no): ").lower() == "yes"

        if has_internet:
            print("Congratulations! You are eligible for the remote job.")
        else:
            print("You need internet access.")

    else:
        print("You need a laptop.")

else:
    print("You must be at least 18 years old.")
    