
def all_left_right_truncatable_prime(x):
    primes = []
    for i in range(2, x+1):
        if is_prime(i) and not '0' in str(i):
            primes.append(i)
    
    truncatable_primes = []
    for prime in primes:
        if is_truncatable_prime(prime, x):
            truncatable_primes.append(prime)
    
    return sorted(truncatable_primes, reverse=True)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n, x):
    while len(str(n)) > 1:
        if not is_prime(int(str(n)[1:])) or int(str(n)[:-1]) % 10 == 0:
            return False
        n //= 10
    
    return True
