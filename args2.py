#concatnation of strings using the concept of *args
def strccat(*str):
    '''function to implement the concept of awrgs by concatnating arbitrary numbers of string'''
    fstr = " "
    for n in str:
        fstr = fstr + n
    return(fstr)
print(strccat.__doc__)
print(strccat("Kushal", " Bhattarai"))
print(strccat("I", " live", " in", " Bhaisepati"))
print(strccat("I"," Love"," One"," Piece"))