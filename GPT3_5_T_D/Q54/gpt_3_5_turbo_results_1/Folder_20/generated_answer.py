
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def right_truncatable_prime(n):
    if not is_prime(n):
        return False
    while n > 10:
        n //= 10
        if not is_prime(n):
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[100]
    results = []
    for i in range(x-1, 9, -1):
        if right_truncatable_prime(i):
            results.append(i)
    return sorted(results, reverse=True)
