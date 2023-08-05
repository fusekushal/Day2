from functools import reduce
def calculate_factorial(n):
    """function to calculate the factorial

    Args:
        n (int): the numbet that we want to calculate factorial for

    Raises:
        ValueError: if the number is below 0 or is negative

    Returns:
        integer: after calculating the factorial it returns it
    """
    if n < 0:
        return "Cannot be calculated as it is below 0!!"
    elif n == 0 & n == 1:
        return 1
    else:
        return reduce(lambda x, y: x*y, range(1, n+1))
    
print(calculate_factorial.__doc__)
num = int(input("Enter a number:"))
print("Factorial of", num,":", calculate_factorial(num))