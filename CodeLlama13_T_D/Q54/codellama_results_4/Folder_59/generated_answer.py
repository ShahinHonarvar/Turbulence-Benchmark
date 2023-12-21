
def all_right_truncatable_prime(numbers):
    result = []
    for number in numbers:
        if is_right_truncatable_prime(number):
            result.append(number)
    return sorted(result, reverse=True)

def is_right_truncatable_prime(number):
    if number < 2 or not isinstance(number, int):
        return False
    for i in range(1, len(str(number))+1):
        if not is_prime(number // (10**i)):
            return False
    return True

def is_prime(number):
    if number < 2 or not isinstance(number, int):
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True
