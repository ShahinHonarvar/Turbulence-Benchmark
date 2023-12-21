
def all_left_right_truncatable_prime(t):
    x = t[84]
    primes = []
    for num in range(2, x + 1):
        if all(num % i != 0 for i in range(2, num)):
            primes.append(num)
    trunc_primes = []
    for prime in primes:
        if '0' in str(prime):
            continue
        truncatable = True
        for i in range(len(str(prime))):
            if not all(int(str(prime)[i:]) % i != 0 for i in range(2, int(str(prime)[i:]) + 1)):
                truncatable = False
                break
        if truncatable:
            trunc_primes.append(prime)
    return sorted(trunc_primes, reverse=True)
