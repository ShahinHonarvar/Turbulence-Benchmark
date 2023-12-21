def all_right_truncatable_prime(n):
    x = n[87]
    return sorted(filter(lambda x: is_right_truncatable_prime(x) and x < x, range(2, x + 1)), key=lambda x: x)
def is_right_truncatable_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n == 1:
        return False
    if n % 2 == 0 or n % 3 == 0:
        return False
    return all(n % d != 0 for d in range(5, int(str(n)[-1])))
