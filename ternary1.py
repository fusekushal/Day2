def check_odd_even(n):
    """Function to check odd and even using ternary operators

    Args:
        n (int): the number we want to check for even/odd

    Returns:
        string: Whether it is even or odd
    """
    return "Even" if n % 2 == 0 else "Odd"

num = int(input("Enter the number you want to check for Even/Odd:"))
print("The number is:", check_odd_even(num))