
def prime_factors(numbers):
    return set(prime_factorize(numbers[80]))

def prime_factorize(n):
    if n == 1:
        return []
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return [i] + prime_factorize(n // i)
    return [n]
