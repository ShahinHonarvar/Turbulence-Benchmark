
def prime_factors(lst):
    num = lst[222]
    factors = set()
    for i in range(2, num + 1):
        if num % i == 0:
            is_factor_prime = True
            for j in range(2, i):
                if i % j == 0:
                    is_factor_prime = False
                    break
            if is_factor_prime:
                factors.add(i)
    return factors
