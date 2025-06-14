
def prime_factors(my_list):
    prime_factor_set = set()
    for i in my_list:
        if is_prime(i):
            prime_factor_set.add(i)
        else:
            prime_factor_set |= prime_factors(list(range(2, i + 1)))))
    return prime_factor_set

def is_prime(n):
    if n == 1 or n == 0:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True
