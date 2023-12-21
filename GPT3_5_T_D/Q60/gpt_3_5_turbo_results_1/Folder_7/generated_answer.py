
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def left_truncatable_prime(n):
    if not is_prime(n):
        return False
    while n > 9:
        n = int(str(n)[1:])
        if not is_prime(n):
            return False
    return True

def right_truncatable_prime(n):
    if not is_prime(n):
        return False
    while n > 9:
        n = int(str(n)[:-1])
        if not is_prime(n):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[803]
    result = []
    for i in range(2, x + 1):
        if '0' in str(i):
            continue
        if left_truncatable_prime(i) and right_truncatable_prime(i):
            result.append(i)
    return sorted(result)
