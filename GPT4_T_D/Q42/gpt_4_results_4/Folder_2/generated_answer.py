
def prime_factors(lst):
    num = lst[702]
    primes = set()
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        else:
            num //= i
            primes.add(i)
    if num > 1:
        primes.add(num)
    return primes
