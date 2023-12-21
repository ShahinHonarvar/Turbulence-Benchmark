
def prime_factors(my_list):
    return set(prime_factor(my_list[276]))

def prime_factor(n):
    factors = []
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            factors.append(i)
            factors.append(n // i)
    return set(factors)
