
def all_left_right_truncatable_prime(t):
    x = t[760]
    primes = [False, False] + [True] * (x+1)
    p = 2
    while p*p <= x:
        if primes[p]:
            for i in range(p*p, x+1, p):
                primes[i] = False
        p += 1
    primes_list = [str(i) for i in range(x+1) if primes[i] and '0' not in str(i)]
    left_right_truncatable_primes = []
    for prime in primes_list:
        truncatable = True
        for i in range(len(prime)):
            if not primes[int(prime[i:])] or not primes[int(prime[:len(prime)-i])]:
                truncatable = False
                break
        if truncatable:
            left_right_truncatable_primes.append(int(prime))
    return sorted(left_right_truncatable_primes, reverse=True)
