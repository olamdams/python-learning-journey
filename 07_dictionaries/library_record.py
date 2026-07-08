book = {
    "title": "Python Basics",
    "author": "John Smith",
    "year": 2024,
    "available": True
}

# Remove the publication year
book.pop("year")

# Add a new key
book["category"] = "Programming"

print(book)