fruits = ["apple", "banana", "orange", "kiwi", "mango"]
del fruits[0]  # deletes the item at index 0, which is "apple"
print(fruits)


# Remove everything from the list
del fruits[:]
print(fruits)

# Clear the list using the clear() method
fruits = ["apple", "banana", "orange", "kiwi", "mango"]
fruits.clear()  # removes all items from the list
print(fruits)
