
def prime_factors(numbers):
    n = numbers[88]
    factors = set()
    i = 2
    while i <= n:
        if n % i == 0:
            factors.add(i)
            n //= i
        else:
            i += 1
    return factors
