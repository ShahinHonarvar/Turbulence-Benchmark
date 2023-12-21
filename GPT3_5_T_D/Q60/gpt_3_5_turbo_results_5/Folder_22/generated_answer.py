
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_and_right_truncatable_prime(n):
    if n < 10:
        return is_prime(n)
    if not is_prime(n):
        return False
    str_n = str(n)
    for i in range(1, len(str_n)):
        if not is_prime(int(str_n[i:])):
            return False
        if not is_prime(int(str_n[:-i])):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[85]
    result = []
    for i in range(10, x + 1):
        if left_and_right_truncatable_prime(i):
            result.append(i)
    return sorted(result)
