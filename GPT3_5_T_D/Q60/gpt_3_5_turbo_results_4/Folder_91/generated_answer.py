
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    if '0' in str(n):
        return False
    digits = len(str(n))
    while digits >= 1:
        if not is_prime(n):
            return False
        n //= 10
        digits -= 1
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[0]
    results = []
    for num in range(x, 1, -1):
        if is_truncatable_prime(num):
            results.append(num)
    return sorted(results, reverse=True)
