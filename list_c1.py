"""Program to create new list that contains strings with more then 5 characters"""
list1 = ["Kushal", "Tom", "Dick", "Harry", "Sushan", "Darshan"]
list_new = [x for x in list1 if len(x)>5]
print(list_new)