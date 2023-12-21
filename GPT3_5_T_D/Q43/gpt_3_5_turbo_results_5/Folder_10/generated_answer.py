
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
    for num in lst[61:80]:
        if is_prime(num):
            primes.append(num)
    return sorted(primes)
