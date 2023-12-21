
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_between_indices(lst):
    primes = [num for i, num in enumerate(lst) if is_prime(num) and 23 <= i <= 59]
    primes.sort(reverse=True)
    return primes
