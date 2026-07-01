score = int(input("Enter your admission score: "))

if score >= 140:
    has_5_olevel_subjects = input(
        "Do you have at least 5 O'Level credits? (yes/no): "
    ).strip().lower()

    if has_5_olevel_subjects == "yes":
        print("Congratulations! You are eligible for admission screening.")
    else:
        print("You need at least 5 O'Level credits.")
else:
    print("Sorry, you are not eligible for admission screening.")
    