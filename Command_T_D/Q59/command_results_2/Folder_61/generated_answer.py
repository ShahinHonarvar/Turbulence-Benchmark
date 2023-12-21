import itertools
def all_left_truncatable_prime(num_range):
    left_truncatable_primes = []
    for n in range(2, num_range[3]):
        s = str(n)
        while s:
            if all(int(c) for c in s):
                break
            s = int(s[1:])
            left_truncatable_primes.append(n)
    return left_truncatable_primes
