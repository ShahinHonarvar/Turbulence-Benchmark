
def all_right_truncatable_prime(x):
    primes = []
    for i in range(10**(x-1), 10**x):
        if is_right_truncatable_prime(i):
            primes.append(i)
    return sorted(primes)

def is_right_truncatable_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
