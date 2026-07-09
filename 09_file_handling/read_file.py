import os
import csv

print("Current working directory:")
print(os.getcwd())

with open("employees.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)