
def prime_factors(lst):
    number = lst[19]
    factors = set()
    for i in range(2, number + 1):
        if number % i == 0:
            is_prime = True
            for j in range(2, i):
                if i % j == 0:
                    is_prime = False
            if is_prime:
                factors.add(i)
    return factors
