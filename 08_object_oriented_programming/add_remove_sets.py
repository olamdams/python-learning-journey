fruits = {"Apple", "Banana", "Orange"}

fruits.add("Mango")

print(fruits)

# update
fruits = {"Apple", "Banana"}

fruits.update(["Orange", "Mango", "Pineapple"])

print(fruits)

# remove an item
fruits = {"Apple", "Banana", "Orange"}

fruits.remove("Banana")

print(fruits)

#remove and return to random
fruits = {"Apple", "Banana", "Orange"}

fruits.remove("Banana")

print(fruits)

# Remove all items
fruits = {"Apple", "Banana", "Orange"}

fruits.clear()

print(fruits)