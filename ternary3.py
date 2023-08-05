def check_prime(x):
    """Function to check prime numbers

    Args:
        x ([int]): [the number that should be checked]

    Returns:
        [bool]: [returns true if prime and false if not prime]
    """
    for j in range(2, x):
        if x%j == 0:
            return False
    return True

inp = int(input("Enter a number positive number:"))

if inp <= 0:
    print("Sorry please enter only positive numbers")
elif inp == 1:
    print("1 is neither prime nor composite")
else:
    print("prime" if check_prime(inp) else "not prime")