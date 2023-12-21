
def all_left_truncatable_prime(numbers):
    return sorted([n for n in numbers if is_left_truncatable_prime(n)], reverse=True)

def is_left_truncatable_prime(n):
    if n < 2:
        return False
    for i in range(1, len(str(n)) + 1):
        if not is_prime(n // 10 ** i):
            return False
    return True

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
