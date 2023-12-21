
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n):
    n = str(n)
    while n:
        if not is_prime(int(n)):
            return False
        n = n[1:]
    return True

def is_right_truncatable_prime(n):
    n = str(n)
    while n:
        if not is_prime(int(n)):
            return False
        n = n[:-1]
    return True

def all_left_right_truncatable_prime(numbers):
    result = []
    x = numbers[25]
    for i in range(2, x + 1):
        if is_prime(i) and '0' not in str(i) and is_left_truncatable_prime(i) and is_right_truncatable_prime(i):
            result.append(i)
    return sorted(result, reverse=True)
