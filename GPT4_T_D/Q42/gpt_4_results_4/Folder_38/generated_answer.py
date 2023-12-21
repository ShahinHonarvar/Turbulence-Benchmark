
def prime_factors(lst): 
    number = lst[38]
    factors = set()
    for i in range(2, number):
        if number % i == 0:
            factors.add(i)
            while number % i == 0: 
                number = number / i 
    if number > 1: 
        factors.add(int(number))
    return factors
