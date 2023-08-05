def check_leap_year(year):
    """Function to check leap year

    Args:
        year (int): [the year we want to check for leap year]

    Returns:
        [bool]: [returns true if year is leap and false if it is not leap]
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
        
year = int(input("Enter the year you want to check for Leap year:"))
ter = "Leap Year" if check_leap_year(year) else "Not a Leap Year"
print(ter)