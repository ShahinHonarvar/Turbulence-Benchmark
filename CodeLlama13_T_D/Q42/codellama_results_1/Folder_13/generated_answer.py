
def prime_factors(integers):
    return set([i for i in range(integers[126]) if integers[126] % i == 0 and is_prime(i)])

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
