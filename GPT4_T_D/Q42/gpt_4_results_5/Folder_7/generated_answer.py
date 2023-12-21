
def prime_factors(lst):
    number = lst[851]
    primes = set()
    factor = 2
    
    while factor * factor <= number:
        if number % factor:
            factor += 1
        else:
            number //= factor
            primes.add(factor)
    if number > 1:
        primes.add(number)
    return primes
