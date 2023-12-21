
def prime_factors(lst):
    
    number = lst[99]
    i = 2
    factors = set()
    while i <= number:
        if (number % i) == 0:
            factors.add(i)
            number = number / i
        else:
            i = i + 1
    return factors
