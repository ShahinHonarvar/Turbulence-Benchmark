
import itertools

def all_left_right_truncatable_prime(test_case):
    for p in itertools.permutations(range(test_case[0], test_case[1] + 1), 3):
        if all(str(p).count(d) == 1 for d in '2357'):
            yield p
    return []
