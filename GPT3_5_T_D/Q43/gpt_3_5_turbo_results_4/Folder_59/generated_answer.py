
def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(lst):
    primes = []
    for i in range(5, 9):
        if i < len(lst) and is_prime(lst[i]):
            primes.append(lst[i])
    return sorted(primes, reverse=True)
