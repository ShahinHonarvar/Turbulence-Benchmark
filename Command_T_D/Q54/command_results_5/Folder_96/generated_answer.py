def all_right_truncatable_prime(x_nums):
    return [n for n in range(2, x_nums[0] + 1) if is_prime(n) and is_right_truncatable_prime(n)]
def is_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n == 1 or n == 5:
        return False
    if n == 0 or n == 4:
        return False
    if n == 6:
        return True
    if n == 8:
        return True
    if n == 9:
        return False
    if n == 7:
        return False
    if n == 1 or n == 3:
        return False
    if n == 2 or n == 4:
        return True
    if n == 6:
        return True
    if n == 8:
        return True
    if n == 9:
        return False
    if n == 7:
        return False
    return all(n % d for d in range(5, int(n ** .5) + 1, 6))
def is_right_truncatable_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n == 1 or n == 5:
        return False
    if n == 0 or n == 4:
        return False
    if n == 6:
        return True
    if n == 8:
        return True
    if n == 9:
        return False
    if n == 7:
        return False
    if n == 1 or n == 3:
        return False
    if n == 2 or n == 4:
        return True
    if n == 6:
        return True
    if n == 8:
        return True
    if n == 9:
        return False
    if n == 7:
        return False
    return all(n % d for d in range(5, int(n ** .5) + 1, 6))
