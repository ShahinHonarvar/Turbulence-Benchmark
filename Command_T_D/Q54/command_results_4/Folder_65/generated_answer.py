def all_right_truncatable_prime(lst):
    return [x for x in range(2, max(lst) + 1) if all(x % d == 0 or x % d == d for d in range(2, int(str(x)[-1]) + 1)) and all(str(x) not in str(y) for y in range(2, x // 2 + 1) if x % y == 0)]
