
def prime_factors(lst):
    num = lst[45]
    factors = set()
    for i in range(2, num):
        if num % i:
            continue
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
        if is_prime:
            factors.add(i)
    return factors
