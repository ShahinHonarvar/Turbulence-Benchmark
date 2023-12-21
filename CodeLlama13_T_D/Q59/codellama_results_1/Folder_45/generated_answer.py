
def all_left_truncatable_prime(numbers):
    result = []
    for num in numbers:
        if is_left_truncatable_prime(num):
            result.append(num)
    return sorted(result)

def is_left_truncatable_prime(n):
    if n < 2 or any(int(str(n)[i]) == 0 for i in range(1, len(str(n)))):
        return False
    for i in range(1, len(str(n))):
        if not is_prime(int(str(n)[:-i])):
            return False
    return True

def is_prime(n):
    if n < 2 or any(n % i == 0 for i in range(2, int(n ** 0.5) + 1)):
        return False
    return True
