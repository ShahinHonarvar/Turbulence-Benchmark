
def all_left_right_truncatable_prime(x):
    l, r = str(x), str(x)[::-1]
    return sorted(x for x in range(2, x + 1) if all(x % 10 != d for d in range(1, x % 10 + 1) if d in l) and all(x % 10 != d for d in range(1, x % 10 + 1) if d in r))
