
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_between_indices(lst):
    primes = []
    for index in range(10, 13):
        if is_prime(lst[index]):
            primes.append(lst[index])
    return sorted(primes)
