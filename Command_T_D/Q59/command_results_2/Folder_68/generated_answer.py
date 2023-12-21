import itertools
def all_left_truncatable_prime(x):
    return sorted(filter(left_truncatable_prime, map(str, range(2, x + 1))), reverse=True)
def left_truncatable_prime(s):
    n = int(s)
    # Check for 0
    if n == 0:
        return False
    # Check for 9
    if n == 9:
        return True
    # Check for 1
    if n == 1:
        return False
    # Check for 2
    if n == 2:
        return True
    # Check for all other numbers
    return all(left_truncatable_prime(str(n - 1)) for n in range(3, int(s) + 1))
