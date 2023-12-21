
def all_left_right_truncatable_prime(n):
    return sorted(set(str(x) for x in range(3, n[0] + 1) if all(str(x) not in str(y) for y in range(x + 1, n[0] + 1) if str(x) in str(y))))
