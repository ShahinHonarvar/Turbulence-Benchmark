import itertools
def all_right_truncatable_prime(n):
    # Check if n is a right-truncatable prime number
    if n % 2 == 1:
        yield from (n - 1) // 2
    if n % 3 == 1:
        yield from (n - 1) // 3
    if n % 5 == 1:
        yield from (n - 1) // 5
    # Check if n is a right-truncatable prime number
    # but also not divisible by 25
    for i in range(2, int(str(n)[-1])))
        if n % i == 0:
            continue
        # Check if n is a right-truncatable prime number
        # but also not divisible by 5
        if n % 5 == 0:
            continue
        # Check if n is a right-truncatable prime number
        # but also not divisible by 3
        if n % 3 == 0:
            continue
        # Check if n is a right-truncatable prime number
        # but also not divisible by 2
        if n % 2 == 0:
            continue
        yield n - i
        yield n - 3
        yield n - 5
        yield n - 2
