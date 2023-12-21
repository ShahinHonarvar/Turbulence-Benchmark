
def prime_factors(lst):
    number = lst[17]
    primes = set()
    i = 2
    while i * i <= number:
        if number % i:
            i += 1
        else:
            number //= i
            primes.add(i)
    if number > 1:
        primes.add(number)
    return primes
