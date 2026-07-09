try:
    with open("employees.csv", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("Error: The file does not exist.")

try:
    with open("employees.csv", "r") as file:
        content = file.read()

except FileNotFoundError:
    print("File not found.")

else:
    print("File opened successfully.")
    print(content)

 try:
    with open("employees.csv", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("File not found.")

finally:
    print("Program finished.")