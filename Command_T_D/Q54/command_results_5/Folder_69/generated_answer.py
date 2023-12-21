import itertools
def all_right_truncatable_prime(n):
    return sorted(filter(lambda p: all(p % i for i in range(2, int(p ** .5) + 1)), (p for p in itertools.permutations(str(n), int(n ** .5) + 1)) if all(p % i == 0 for i in range(2, int(p ** .5) + 1)))), reverse=True)
