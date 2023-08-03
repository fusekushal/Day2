def return_sum(**kwargs):
    '''function to implement kwargs in python'''
    price = 0
    for _, v in kwargs.items():
        price = price + v
    return price

print(return_sum.__doc__)
print(return_sum(tomato=150, Ginger=430, Garlic=410))
print(return_sum(lays=75, nuggets=350, bhujia=240, kurkure=50))