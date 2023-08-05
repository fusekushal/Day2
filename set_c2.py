"""Second program to implement set comprehensions"""
words = ["Kushal", "Nayan", "Darshan"]
final = {char for word in words for char in word}
print(final)