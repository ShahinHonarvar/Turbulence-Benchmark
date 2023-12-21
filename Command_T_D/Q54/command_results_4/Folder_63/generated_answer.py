def all_right_truncatable_prime(x):
    res = []
    while len(res) < x[0]:
        # Find all primes that are right-truncatable
        for n in range(3, int(x[0] ** .5) + 1):
            c = str(n)
            while c[-1] in '2357':
                n //= 10**(len(c) - 1)
                c = str(n)
            if all(n % i for i in range(3, int(x[0] ** .5) + 1)):
                res += [n]
    return res
