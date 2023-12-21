
def all_left_right_truncatable_prime(x):
    from itertools import count
    from math import sqrt
    if sqrt(x) * 2 - 1 <= 1:
        return []
    return sorted(filter(left_right_truncatable_prime, (n for n in count(2, x // 2) if n <= x)), reverse=True)

def left_right_truncatable_prime(x):
    from functools import reduce
    if x <= 1:
        return True
    return reduce(lambda a, b: a and b, (left_right_truncatable_prime(n) for n in range(2, x // 2 + 1)))
