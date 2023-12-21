def all_right_truncatable_prime(n):
    return [str(y) for y in range(n[0] + 1, n[1] + 1) if all(str(x) == str(x - 1) for x in range(y, n[0] + 1) if x == y or str(x) == str(x - 1))]
