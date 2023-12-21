import itertools
def all_right_truncatable_prime(args):
    return sorted(
        [n for n in itertools.filter(
            lambda x: all(n % d == 0 for d in range(2, int(str(x)[-1]) + 1)),
            args[50] - 1
        )],
        reverse=True
    )
