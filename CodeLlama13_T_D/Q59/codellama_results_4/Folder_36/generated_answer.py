
def all_left_truncatable_prime(x):
    primes = []
    for i in range(2, x+1):
        if is_prime(i) and '0' not in str(i):
            primes.append(i)
    
    left_truncatable_primes = []
    for p in primes:
        temp = p
        while temp > 0:
            if is_prime(temp):
                left_truncatable_primes.append(p)
                break
            temp //= 10
    
    return sorted(left_truncatable_primes)
