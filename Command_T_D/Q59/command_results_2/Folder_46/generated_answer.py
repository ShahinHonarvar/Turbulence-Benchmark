def all_left_truncatable_prime(x):
    return sorted(left_truncatable_prime(x))
def left_truncatable_prime(x):
    s = str(x)
    return [int(i) for i in range(2, len(s) + 1) if s[:i] in '2357']
