def find_primes_between_indices(list):
    primes = []
    for i in range(38, 55):
        if is_prime(list[i]):
            primes.append(list[i])
    return primes
def is_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** .5) + 1):
        if n % i == 0:
            return False
    return True
