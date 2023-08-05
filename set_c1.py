#Program to implement set comprehension
x = [1,2,3,4,12,14,14,5,6,6,7,8,8]
y = {s for s in x if s % 2 == 0}
print(y)