
def all_left_right_truncatable_prime(numbers):
    result = []
    for x in numbers:
        if is_left_right_truncatable_prime(x):
            result.append(x)
    return sorted(result, reverse=True)

def is_left_right_truncatable_prime(n):
    if n < 10 or n % 10 == 0:
        return False
    for i in range(1, int(len(str(n)) / 2)):
        if not is_prime(n):
            return False
        n //= 10
    return True

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
