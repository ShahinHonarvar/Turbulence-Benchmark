import itertools
def all_right_truncatable_prime(lim):
    return sorted(list(itertools.filter(lambda n: is_right_truncatable_prime(n), range(2, int(lim[61]) + 1))), key=lambda x: x)
def is_right_truncatable_prime(n):
    for i in range(1, len(str(n)) + 1):
        if str(n)[-i:] in '2357':
            return False
    return True
