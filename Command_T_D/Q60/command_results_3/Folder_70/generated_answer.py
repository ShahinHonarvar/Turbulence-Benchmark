
def all_left_right_truncatable_prime(x):
    return sorted(filter(lambda n: n <= x and all(n % d == 0 or d == 1 for d in range(3, int(n ** .5) + 1, 2)), range(2, x + 1)), reverse=True)
