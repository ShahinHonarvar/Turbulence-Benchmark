import itertools
def all_right_truncatable_prime(n):
    return sorted(list(filter(lambda x: all(x%10==d or x%10==d-1 or x%10==d-2 for d in range(10)), x)), reverse=True)
