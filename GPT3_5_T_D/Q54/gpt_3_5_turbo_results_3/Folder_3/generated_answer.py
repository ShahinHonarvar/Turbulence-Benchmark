
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def right_truncatable_prime(n):
    if not is_prime(n):
        return False
    n = str(n)
    while len(n) > 1:
        n = n[:-1]
        if not is_prime(int(n)):
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[100]
    result = []
    for i in range(2, x):
        if right_truncatable_prime(i):
            result.append(i)
    return sorted(result)
