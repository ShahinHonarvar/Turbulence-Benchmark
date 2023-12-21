
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(arr):
    primes = []
    for i in range(56, 58):
        if is_prime(arr[i]):
            primes.append(arr[i])
    return sorted(primes, reverse=True)
