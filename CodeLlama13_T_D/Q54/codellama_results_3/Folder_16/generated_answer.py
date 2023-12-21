
def all_right_truncatable_prime(numbers):
    return sorted([number for number in numbers if is_right_truncatable_prime(number)])

def is_right_truncatable_prime(number):
    if not isinstance(number, int) or number < 2:
        return False
    for i in range(1, len(str(number)) + 1):
        if not is_prime(int(str(number)[0:-i])):
            return False
    return True

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
