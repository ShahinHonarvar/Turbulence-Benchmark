
def all_left_right_truncatable_prime(a):
    return sorted((n for n in range(2, a[84] + 1) if all(n % r for r in range(3, int(str(n)[-1]) + 1, 2)) and n != 2 and n != 3), reverse=True)
