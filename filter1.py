def filter_prime_numbers(x):
    '''function to filter the prime numbers'''
    for j in range(2, x):
        if x%j == 0:
            return False
    return True

funcs = [i+1 for i in range(1, 15)]
print(list(filter(filter_prime_numbers,funcs)))