def find_primes_between_indices(list):
    primes = []
    for i in range(len(list) - 1):
        if is_prime(list[i]):
            primes.append(list[i])
            break
    return primes
def is_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    maxDivisor = n**0.5
    i = 5
    while i <= maxDivisor:
        if n % i == 0:
            return False
        i += 6
    return True
