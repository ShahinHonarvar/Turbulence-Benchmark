
def is_prime(n):
    if n == 1 or n == 0:
        return False
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
    return True

def find_primes_between_indices(lst):
    primes = []
    for i in range(61, 80):
        if i < len(lst) and is_prime(lst[i]):
            primes.append(lst[i])
    primes.sort()
    return primes
