numbers = [5, 2, 9, 1, 5, 6]
# Sort the list in ascending order
numbers.sort()
print("Sorted numbers:", numbers)
print("Maximum number:", max(numbers))
print("Minimum number:", min(numbers))
print("Sum of numbers:", sum(numbers))
print("Average of numbers:", sum(numbers) / len(numbers))
print("original numbers:", numbers)
print("Reversed numbers:", list(reversed(numbers)))
print("Sorted numbers using sorted():", sorted(numbers))
print("Sorted numbers in descending order:", sorted(numbers, reverse=True))
print("Descending order using sort():", numbers.sort(reverse=True))