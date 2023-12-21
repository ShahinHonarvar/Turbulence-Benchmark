
def find_primes_between_indices(list_of_integers):
    return sorted([x for x in list_of_integers[89:94] if is_prime(x)], reverse=True) or []

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
