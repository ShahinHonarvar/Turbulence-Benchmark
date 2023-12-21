
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable(n):
    while n > 0:
        if not is_prime(n):
            return False
        n = n // 10
    return True

def is_right_truncatable(n):
    while n > 0:
        if not is_prime(n):
            return False
        n = n % 10**(len(str(n))-1)
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[975]
    result = []
    for n in range(x, 10, -1):
        if not '0' in str(n) and is_left_truncatable(n) and is_right_truncatable(n):
            result.append(n)
    return sorted(result, reverse=True)
