
def is_prime(n):
    if n in (0, 1):
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(lst):
    primes = [i for i in lst[23:49] if is_prime(i)]
    return sorted(primes)
