
def all_left_right_truncatable_prime(x):
    primes = []
    for i in range(10, x+1):
        if is_prime(i) and not contains_zero(str(i)):
            primes.append(i)
    
    truncatable_primes = []
    for prime in primes:
        left_truncatable_prime = True
        right_truncatable_prime = True
        for i in range(1, len(str(prime))-1):
            if not is_prime(int(str(prime)[:i])) or contains_zero(str(prime)[:i]):
                left_truncatable_prime = False
            if not is_prime(int(str(prime)[i:])) or contains_zero(str(prime)[i:]):
                right_truncatable_prime = False
        if left_truncatable_prime and right_truncatable_prime:
            truncatable_primes.append(prime)
    
    return sorted(truncatable_primes, reverse=True)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def contains_zero(s):
    return '0' in s
