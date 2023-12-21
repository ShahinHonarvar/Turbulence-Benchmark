
def all_left_right_truncatable_prime(x):
    return sorted([p for p in range(2, x + 1) if is_truncatable_prime(p)])

def is_truncatable_prime(n):
    if n < 2 or not is_prime(n):
        return False
    for i in range(len(str(n)) - 1, 0, -1):
        if not is_prime(int(str(n)[:i])):
            return False
    return True

def is_prime(n):
    if n < 2 or any(n % i == 0 for i in range(2, int(n ** 0.5) + 1)):
        return False
    return True
