
def prime_factors(numbers):
    return set(prime_factorization(numbers[69]))

def prime_factorization(n):
    factors = []
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            factors.append(i)
            factors.extend(prime_factorization(n / i))
            break
    else:
        factors.append(n)
    return factors
