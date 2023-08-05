#implementing list comprehension to find product between each corresponding elements in two list
x = [2,4,6,8]
y = [8,6,4,2]
new_list = [x[i]*y[i] for i in range(0, len(x))]
print(new_list)