
def all_left_right_truncatable_prime(args):
    return sorted(x for x in range(2, args[0] + 1) if all(x % 2 == 0 or x % 5 == 0 or x % 10 == 0 or x % 15 == 0 or x % 30 == 0 or x % 105 == 0 for x in range(x, x + 100, 5)))
