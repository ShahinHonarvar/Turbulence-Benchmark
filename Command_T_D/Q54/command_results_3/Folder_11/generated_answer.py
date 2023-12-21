import sys
def all_right_truncatable_prime(test_tup):
    x = test_tup[86]
    primes = set()
    for i in range(2, x // 2):
        j = str(i)
        while j and j[-1] != '9':
            j = int(j[0:-1])
        if i == j:
            primes.add(i)
    return sorted(list(primes))
