
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(n):
    str_n = str(n)
    if '0' in str_n:
        return False
    for i in range(len(str_n)):
        left = int(str_n[:i + 1])
        right = int(str_n[i:])
        if not is_prime(left) or not is_prime(right):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[32]
    result = []
    for i in range(2, x + 1):
        if is_left_right_truncatable_prime(i):
            result.append(i)
    return result
