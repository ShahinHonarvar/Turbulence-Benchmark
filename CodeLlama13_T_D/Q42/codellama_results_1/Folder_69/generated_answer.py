
def prime_factors(numbers):
    return set(prime_factorize(numbers[459]))

def prime_factorize(n):
    i = 2
    factors = []
    while n > 1:
        if n % i == 0:
            factors.append(i)
            n //= i
        else:
            i += 1
    return factors
