
def find_primes_between_indices(numbers):
    primes = []
    for i in range(19, 90+1):
        if is_prime(i):
            primes.append(i)
    return sorted(primes, reverse=True)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True
