
def all_left_right_truncatable_prime(x):
    return sorted([i for i in range(2, x + 1) if is_left_right_truncatable_prime(i)])

def is_left_right_truncatable_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
