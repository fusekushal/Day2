def add(*num):
    sum = 0
    
    for n in num:
        sum = sum + n

    return(sum)

print(add(3, 5, 6, 7, 8))
print(add(4,5,6,3,2,3,1,3,3,3,4,5,5,5,2))
print(add(5.3, 5.4, 2.4, 2))
print(int(add(5.3, 5.4, 2.4, 2)))