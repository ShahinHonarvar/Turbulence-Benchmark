
import itertools

def all_left_right_truncatable_prime(lim):
    """
    Input: lim (a tuple of positive integers)
    Returns: a list of all left-and-right-truncatable prime numbers less than or equal to x
    """
    nums = range(2, lim[0])
    for l in range(1, lim[1]):
        nums += [n for n in itertools.permutations(str(l), 2) if n[0] in "2357" and n[1] in "2357"]
    return sorted(nums)
