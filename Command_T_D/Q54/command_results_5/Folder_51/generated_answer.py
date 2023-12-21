import sys
def all_right_truncatable_prime(test_tup):
    x = test_tup[54]
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
    for prime in primes:
        if prime < x:
            if prime * 10 ** (len(str(x)) - 1) <= x:
                continue
            else:
                break
        elif prime == x:
            continue
        elif prime > x:
            break
    return primes
