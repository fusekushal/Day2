def square_numbers(x):
    """Function to return the square of numbers

    Args:
        x (int): the number that we want to find square for

    Returns:
        int: the square of the number that we passed
    """
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