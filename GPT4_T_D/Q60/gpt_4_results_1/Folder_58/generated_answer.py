
import itertools
    
def all_left_right_truncatable_prime(t):
    def get_primes(n):
        sieve = [True] * n
        for x in range(2, int(n ** 0.5) + 1):
            for i in range(x*2, n, x):
                sieve[i] = False
        return [2] + [i for i in range(3, n, 2) if sieve[i]]

    def left_right_truncatable(primes, n):
        primes_set = set(primes)
        str_n = str(n)
        for i in range(len(str_n)):
            if int(str_n[i:]) not in primes_set or int(str_n[:len(str_n) - i]) not in primes_set:
                return False
        return True
    
    limit = t[975]
    primes = get_primes(limit)
    primes_without_zero = [p for p in primes if '0' not in str(p)]
    left_right_truncatable_primes = [p for p in primes_without_zero if left_right_truncatable(primes, p)]
    return sorted(left_right_truncatable_primes, reverse=True)
