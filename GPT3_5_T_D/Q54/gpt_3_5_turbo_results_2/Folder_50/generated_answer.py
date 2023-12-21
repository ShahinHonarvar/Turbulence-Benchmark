
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def right_truncatable(n):
    if not is_prime(n):
        return False
    while n > 0:
        if not is_prime(n):
            return False
        n //= 10
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[57]
    result = []
    for i in range(2, x):
        if right_truncatable(i):
            result.append(i)
    return sorted(result, reverse=True)
