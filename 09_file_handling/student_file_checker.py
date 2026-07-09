filename = input("Enter the filename: ")

try:
    with open(filename, "r") as file:
        print("\nFile Contents:")
        print(file.read())

except FileNotFoundError:
    print("Sorry! That file does not exist.")

finally:
    print("\nThank you for using the program.")
    