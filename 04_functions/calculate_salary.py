def salary(name, basic_salary, bonus):
    total_salary = basic_salary + bonus
    return f"{name} earns {total_salary} per month."

salary = salary(
    name="Olamide", 
    basic_salary=550000, 
    bonus=100000)

print(salary)
