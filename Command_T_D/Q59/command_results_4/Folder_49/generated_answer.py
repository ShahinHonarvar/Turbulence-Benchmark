import itertools
def all_left_truncatable_prime(n):
    primes = [x for x in range(2, int(n[14])+1) if all(x%y!=0 for y in range(2, x//2+1)) and all(x%y!=0 for y in range(x, x-1, -1))]
    return sorted(list(itertools.chain.from_iterable(itertools.permutations(primes, len(primes)))))
