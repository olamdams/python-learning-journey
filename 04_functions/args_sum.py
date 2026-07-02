def add_numbers(*numbers):
    total = 0

    for number in numbers:
        total += number

    return total

print(add_numbers(5, 10))
print(add_numbers(5, 10, 15))
print(add_numbers(5, 10, 15, 20))