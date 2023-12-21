
def all_left_right_truncatable_prime(numbers):
    result = []
    for num in numbers:
        if is_left_and_right_truncatable_prime(num):
            result.append(num)
    return sorted(result, reverse=True)

def is_left_and_right_truncatable_prime(num):
    if num < 2:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0 or contains_zero(str(i)):
            return False
    return True

def contains_zero(s):
    return '0' in s
