""" using the concept of dictionary comprehension to solve 
Given two lists - one containing keys and another containing values,
create a dictionary using dictionary comprehension.
"""
x = [1,2,3,4]
y = [1,4,9,16]

z = {k:v for k,v in zip(x,y)}
print(z)