
def all_left_right_truncatable_prime(n):
    return sorted(x for x in range(2, int(str(n)[-1]) + 1) if all(x % 10**i == 1 for i in range(1, int(str(x)))))
