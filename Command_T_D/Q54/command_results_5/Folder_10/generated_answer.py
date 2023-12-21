import bisect
def all_right_truncatable_prime(x):
    return sorted(set(range(2, int(str(x)[-1]) + 1)), reverse=True) if bisect.insort_left(x, 2) else [])
