
def all_left_truncatable_prime(t):
    from itertools import permutations
    from sympy import isprime

    x = t[767]
    primes = []
    for n in range(1, len(str(x))):
        perms = permutations('123456789', n)
        for p in perms:
            num = int(''.join(p))
            if num < x:
                if isprime(num):
                    truncatable = True
                    for i in range(1, len(str(num))):
                        if not isprime(int(str(num)[i:])):
                            truncatable = False
                            break
                    if truncatable:
                        primes.append(num)
    return sorted(primes, reverse=True)
