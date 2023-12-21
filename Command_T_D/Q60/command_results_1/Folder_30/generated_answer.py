
def all_left_right_truncatable_prime(n):
    return sorted(n for n in range(3, int(n[0]) + 1) if all(str(n) not in x for x in range(2, int(str(n)) + 1)))
