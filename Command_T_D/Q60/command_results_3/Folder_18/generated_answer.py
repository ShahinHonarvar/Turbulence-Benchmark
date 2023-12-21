
import itertools

def all_left_right_truncatable_prime(n):
    p = iter(itertools.permutations(str(n), 3))
    return sorted(list(filter(lambda x: all(str(x) in "2357" or str(x) in "2357\1" for x in range(2, int(str(x)[-1]) + 1)), n)), key=lambda x: x)
