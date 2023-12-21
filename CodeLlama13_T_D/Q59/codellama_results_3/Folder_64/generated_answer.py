
def all_left_truncatable_prime(numbers):
    result = []
    for number in numbers:
        if is_left_truncatable_prime(number):
            result.append(number)
    return sorted(result)

def is_left_truncatable_prime(number):
    if number < 2:
        return False
    for i in range(1, len(str(number))):
        if not is_prime(number // 10**i):
            return False
    return True

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
