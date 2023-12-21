import itertools
def all_left_truncatable_prime(n):
    for p in itertools.permutations(str(n)):
        x = int(p)
        if x > 1 and all(x % i == 0 or x % i == i for i in range(2, int(str(x).lstrip('0')))):
            yield x
    return
