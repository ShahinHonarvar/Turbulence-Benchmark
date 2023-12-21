
def all_left_truncatable_prime(numbers):
    result = []
    for number in numbers:
        if is_left_truncatable_prime(number):
            result.append(number)
    return sorted(result, reverse=True)

def is_left_truncatable_prime(number):
    if not isinstance(number, int) or number <= 0:
        return False
    digits = list(str(number))
    for i in range(len(digits)):
        if '0' in digits[:i]:
            return False
        if not is_prime(int(''.join(digits[i:]))):
            return False
    return True

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True
