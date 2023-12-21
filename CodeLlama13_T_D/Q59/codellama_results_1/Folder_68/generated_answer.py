
def all_left_truncatable_prime(numbers):
    return sorted([x for x in range(*numbers) if is_left_truncatable_prime(x)], reverse=True)

def is_left_truncatable_prime(n):
    if n < 2:
        return False
    for i in range(1, int(len(str(n)) / 2)):
        if '0' in str(n) or not is_prime(n):
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
