def square_numbers(x):
    return (x*x)

funcs = [square_numbers]
lst = [1, 2, 3, 4, 5]
li = []
for i in lst:
    value = list(map(lambda x: x(i), funcs))
    li.append(value)

lii = [i[0] for i in li]
print("The original list is", lst)
print("The squared list is", lii)