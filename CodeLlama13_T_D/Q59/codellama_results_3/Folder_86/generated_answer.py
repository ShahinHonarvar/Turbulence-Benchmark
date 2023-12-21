
def all_left_truncatable_prime(x):
    x = int(x)
    primes = []
    for i in range(2, x+1):
        if is_prime(i) and not contains_0(str(i)):
            primes.append(i)
    
    left_truncatable_primes = []
    for p in primes:
        s = str(p)
        while len(s) > 1:
            if not is_prime(int(s[1:])):
                break
            left_truncatable_primes.append(p)
            s = s[1:]
    
    return sorted(left_truncatable_primes, reverse=True)
