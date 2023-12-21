
def all_left_right_truncatable_prime(numbers):
    return sorted([x for x in range(*numbers) if is_left_right_truncatable_prime(x)])

def is_left_right_truncatable_prime(n):
    if n < 10:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0 or not is_prime(i) or not is_prime(n // i):
            return False
    return True

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
