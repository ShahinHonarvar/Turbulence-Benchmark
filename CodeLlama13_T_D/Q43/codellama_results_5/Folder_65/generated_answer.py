
def find_primes_between_indices(my_list):
    return sorted(set([x for i, x in enumerate(my_list) if 76 <= i <= 92 and is_prime(x)]))

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
