
def is_prime(n):
    if n == 0 or n == 1:
        return False
        
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def find_primes_between_indices(lst):
    primes = [i for i in lst[61:81] if is_prime(i)]
    return sorted(primes, reverse=True)
