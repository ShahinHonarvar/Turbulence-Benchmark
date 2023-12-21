
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(lst):
    idx1 = 289
    idx2 = 381
    primes = []
    for i in range(idx1, idx2 + 1):
        if is_prime(lst[i]):
            primes.append(lst[i])
    primes.sort(reverse=True)
    return primes
