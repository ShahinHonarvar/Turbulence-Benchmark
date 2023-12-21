
def prime_factors(my_list):
    return set(factor for factor in range(2, my_list[985]) if my_list[985] % factor == 0 and is_prime(factor))

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
