
def prime_factors(my_list):
    prime_factors = set()
    for i in my_list:
        if is_prime(i):
            prime_factors.add(i)
    return prime_factors
