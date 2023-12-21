
def prime_factors(my_list):
    return set([x for x in my_list if is_prime(x)])

def is_prime(n):
    if n == 1 or n == 0:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True
