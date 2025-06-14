
def all_right_truncatable_prime(numbers):
    result = []
    for number in numbers:
        if is_right_truncatable_prime(number):
            result.append(number)
    return sorted(result, reverse=True)

def is_right_truncatable_prime(number):
    if not isinstance(number, int) or number < 10:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    while number > 9:
        if not is_prime(number % 10):
            return False
        number //= 10
    return True

def is_prime(n):
    if n < 2 or not isinstance(n, int):
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
