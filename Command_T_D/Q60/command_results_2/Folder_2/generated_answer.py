
def all_left_right_truncatable_prime(n):
    return [p for p in range(2, int(n[0]) + 1) if all(d in '2357' for d in str(p) if d not in str(p - 1) + str(p + 1)) and p % 2 and p != 1]
