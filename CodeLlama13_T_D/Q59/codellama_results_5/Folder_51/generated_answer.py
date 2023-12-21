
def all_left_truncatable_prime(numbers):
    result = []
    for num in numbers:
        if is_prime(num) and contains_no_zero(str(num)):
            result.append(num)
    return sorted(result)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def contains_no_zero(s):
    return '0' not in s
