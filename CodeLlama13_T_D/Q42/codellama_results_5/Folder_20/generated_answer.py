
def prime_factors(my_list):
    return set(prime_factorizer(my_list[53]))

def prime_factorizer(n):
    i = 2
    factors = []
    while n > 1:
        if n % i == 0:
            factors.append(i)
            n /= i
        else:
            i += 1
    return factors
