
def all_left_truncatable_prime(x):
    primes = []
    for i in range(10**64, x+1):
        if is_left_truncatable_prime(i):
            primes.append(i)
    return sorted(primes, reverse=True)

def is_left_truncatable_prime(n):
    if n % 2 == 0 or n % 5 == 0:
        return False
    for i in range(1, int(n**0.5)+1):
        if n % i == 0 and str(i) not in str(n):
            return False
    return True
