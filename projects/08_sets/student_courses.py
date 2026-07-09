python_students = {"Olamide", "Grace", "David", "Aisha"}
sql_students = {"Grace", "David", "John", "Fatima"}
print("Python Students:", python_students)
print("SQL Students:", sql_students)

print("\nUnion:")
print(python_students | sql_students)

print("\nIntersection:")
print(python_students & sql_students)

print("\nPython Only:")
print(python_students - sql_students)

print("\nSQL Only:")
print(sql_students - python_students)

print("\nSymmetric Difference:")
print(python_students ^ sql_students)


#Imagine you have two customer lists:
website_customers = {"Alice", "Bob", "David"}
store_customers = {"Bob", "Grace", "David"}

print("Customers in both:", website_customers & store_customers)
print("All customers:", website_customers | store_customers)
print("Online only:", website_customers - store_customers)