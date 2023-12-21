
def all_right_truncatable_prime(numbers):
    result = []
    for n in numbers:
        if is_right_truncatable_prime(n):
            result.append(n)
    return sorted(result, reverse=True)

def is_right_truncatable_prime(n):
    if n <= 1 or any(n % i == 0 for i in range(2, int(n ** 0.5) + 1)):
        return False
    for i in range(len(str(n)) - 1, 0, -1):
        if not is_prime(int(str(n)[:i])):
            return False
    return True

def is_prime(n):
    if n <= 1 or any(n % i == 0 for i in range(2, int(n ** 0.5) + 1)):
        return False
    return True
