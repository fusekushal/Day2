#Program to implement dictionary comprehension
student = {'Kushal':93, 'Tom':48, 'Dick':68, 'Harry':81, 'Darshan':95}
good_student = {k:v for (k,v) in student.items() if v>80 }
print(good_student)