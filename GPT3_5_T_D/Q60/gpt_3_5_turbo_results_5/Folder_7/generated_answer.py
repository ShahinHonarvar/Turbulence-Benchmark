
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    def is_left_right_truncatable_prime(n):
        if '0' in str(n):
            return False
        if not is_prime(n):
            return False
        digits = str(n)
        while len(digits) > 2:
            digits = digits[1:-1]
            if not is_prime(int(digits)):
                return False
        return True

    x = numbers[803]
    result = []
    for i in range(2, x + 1):
        if is_left_right_truncatable_prime(i):
            result.append(i)
    result.sort()
    return result
