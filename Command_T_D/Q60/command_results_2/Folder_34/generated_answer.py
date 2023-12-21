
def all_left_right_truncatable_prime(n):
    return [x for x in range(2, n[18] + 1) if x % 2 == 1 and all(x % d == 0 or x % d == d for d in range(3, int(x ** .5) + 1, 2)) and x not in [2, 3, 5, 7, 11, 13, 17, 19]]
