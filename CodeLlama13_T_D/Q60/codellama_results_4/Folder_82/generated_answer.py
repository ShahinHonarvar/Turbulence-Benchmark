
def all_left_right_truncatable_prime(x):
    primes = []
    for i in range(10, x+1):
        if is_prime(i) and not contains_zero(str(i)):
            primes.append(i)
    
    left_right_truncatable_primes = []
    for prime in primes:
        if is_left_and_right_truncatable_prime(prime):
            left_right_truncatable_primes.append(prime)
    
    return sorted(left_right_truncatable_primes, reverse=True)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def contains_zero(s):
    return '0' in s

def is_left_and_right_truncatable_prime(n):
    while len(str(n)) > 1:
        if not is_prime(n):
            return False
        n = int(str(n)[1:-1])
    return True
