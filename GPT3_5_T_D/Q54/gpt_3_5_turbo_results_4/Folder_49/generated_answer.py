
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable(n):
    while n >= 10:
        n //= 10
        if not is_prime(n):
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[14]
    result = []
    for i in range(2, x):
        if is_prime(i) and is_right_truncatable(i):
            result.append(i)
    return sorted(result)
