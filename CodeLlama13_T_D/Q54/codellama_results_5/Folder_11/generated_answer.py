
def all_right_truncatable_prime(numbers):
    result = []
    for x in numbers:
        if is_right_truncatable_prime(x):
            result.append(x)
    return sorted(result)

def is_right_truncatable_prime(n):
    if n < 10:
        return False
    while n > 0:
        if not is_prime(n):
            return False
        n //= 10
    return True

def is_prime(n):
    if n == 1 or n == 0:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
