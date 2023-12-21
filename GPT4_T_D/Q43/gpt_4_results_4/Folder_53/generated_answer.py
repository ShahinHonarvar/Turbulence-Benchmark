
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def find_primes_between_indices(lst):
    primes = []
    for i in range(43, min(len(lst), 60)):
        if is_prime(lst[i]):
            primes.append(lst[i])
    primes.sort(reverse=True)
    return primes
