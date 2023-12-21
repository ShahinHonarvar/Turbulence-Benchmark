
def prime_factors(my_list):
    return set([x for x in range(2, my_list[714]) if my_list[714] % x == 0 and is_prime(x)])

def is_prime(n):
    return all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))
