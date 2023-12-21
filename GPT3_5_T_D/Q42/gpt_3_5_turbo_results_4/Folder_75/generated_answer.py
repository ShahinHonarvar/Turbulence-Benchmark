
def prime_factors(numbers):
    n = numbers[80]
    factors = set()
    i = 2
    while i <= n:
        if n % i == 0:
            factors.add(i)
            n = n / i
        else:
            i += 1
    return factors
