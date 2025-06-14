
def all_left_right_truncatable_prime(x):
    primes = []
    for i in range(2, x+1):
        if is_prime(i) and not '0' in str(i):
            primes.append(i)
    
    truncatable_primes = []
    for p in primes:
        left_truncatable = True
        right_truncatable = True
        for i in range(1, len(str(p))):
            if not is_prime(int(str(p)[:i])) or str(p)[i:] == '':
                left_truncatable = False
            if not is_prime(int(str(p)[i:])) or str(p)[:i] == '':
                right_truncatable = False
        if left_truncatable and right_truncatable:
            truncatable_primes.append(p)
    
    return sorted(truncatable_primes, reverse=True)

def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
