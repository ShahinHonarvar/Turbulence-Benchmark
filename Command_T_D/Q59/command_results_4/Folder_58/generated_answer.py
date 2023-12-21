import itertools
def all_left_truncatable_prime(n):
    x = n[-1]
    # Find all left-truncatable primes less than x
    return sorted(list(filter(lambda n: all(n % d for d in range(2, int(n ** .5) + 1)),  # n is prime
                             (n for n in itertools.permutations(str(x)) if all(int(i) for i in str(n))))))
