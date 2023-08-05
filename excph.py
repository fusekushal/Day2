x = int(input("Please Enter the Numerator:"))
y = int(input("Please Enter the Denominator:"))
try:
    result = x/y
    print(result)
except:
    print("Error: Denominator cannot be 0.")