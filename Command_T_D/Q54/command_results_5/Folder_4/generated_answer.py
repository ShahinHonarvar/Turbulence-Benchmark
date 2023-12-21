import sys
def all_right_truncatable_prime(lims):
    return sorted(list(filter(lambda x: is_right_truncatable_prime(x) and x < lims[96], range(2, lims[96] + 1))), reverse=True)
def is_right_truncatable_prime(n):
    return all(n % d != 0 for d in range(2, int(n ** .5) + 1))
