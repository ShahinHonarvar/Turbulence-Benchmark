
def all_left_right_truncatable_prime(l):
    return sorted((x for x in range(l[14], 1, -1) if all(x % d for d in range(3, int(str(x)[-1]) + 1, 2)), key=lambda x: x) or [])
