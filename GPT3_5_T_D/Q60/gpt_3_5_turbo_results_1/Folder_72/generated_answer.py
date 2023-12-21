
def all_left_right_truncatable_prime(numbers):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_truncatable_prime(num):
        if '0' in str(num):
            return False
        if not is_prime(num):
            return False
        left_digits = str(num)
        right_digits = str(num)
        while len(left_digits) >= 2:
            left_digits = left_digits[1:]
            if not is_prime(int(left_digits)):
                return False
        while len(right_digits) >= 2:
            right_digits = right_digits[:-1]
            if not is_prime(int(right_digits)):
                return False
        return True

    x = numbers[31]
    result = []
    for i in range(x, 0, -1):
        if is_truncatable_prime(i):
            result.append(i)
    return result
