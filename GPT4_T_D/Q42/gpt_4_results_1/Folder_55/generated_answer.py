
def prime_factors(list):
    num = list[21]
    primes = set()
    divisor = 2
    while divisor <= num:
        if (num % divisor) == 0:
            primes.add(divisor)
            num = num/divisor
        else:
            divisor += 1
    return primes
