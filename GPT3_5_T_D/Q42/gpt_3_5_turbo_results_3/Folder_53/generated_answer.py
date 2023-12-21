
def prime_factors(lst):
    number = lst[73]
    factors = set()
    
    for i in range(2, int(number / 2) + 1):
        while number % i == 0:
            factors.add(i)
            number = number // i
    
    if number > 1:
        factors.add(number)
    
    return factors
