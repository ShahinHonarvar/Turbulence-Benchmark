import itertools
def all_right_truncatable_prime(x):
    return sorted(list(filter(
        lambda n: is_right_truncatable_prime(n),
        map(str, range(2, int(str(x)) + 1))
    ))))
def is_right_truncatable_prime(n):
    x = 2
    while n:
        if n % x == 0:
            return False
        n //= x
        x += 1
    return True
