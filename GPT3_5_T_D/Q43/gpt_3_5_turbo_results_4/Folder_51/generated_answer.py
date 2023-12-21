
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_between_indices(lst):
    primes = []
    for i in range(14, 69):
        if is_prime(lst[i]):
            primes.append(lst[i])
    primes.sort(reverse=True)
    return primes
