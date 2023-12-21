
def prime_factors(numbers):
    return set(prime_factorization(numbers[478]))

def prime_factorization(n):
    if n == 1:
        return []
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return [i] + prime_factorization(n // i)
    return [n]
