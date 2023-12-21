import itertools
def all_left_truncatable_prime(test_case):
    #  3 compatibility:
    # itertools.permutations is a  3 keyword.
    # itertools.permutations(test_case[70])
    # gives an error in  2.7.8
    return sorted(set(test_case[70] - 1) for _ in range(70))
