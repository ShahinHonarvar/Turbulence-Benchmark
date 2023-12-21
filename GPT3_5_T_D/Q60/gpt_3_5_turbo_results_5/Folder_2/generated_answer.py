
def all_left_right_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        str_n = str(n)
        for i in range(1, len(str_n)):
            left = int(str_n[:i])
            right = int(str_n[-i:])
            if not is_prime(left) or not is_prime(right):
                return False
        return True

    x = numbers[618]
    result = []
    for i in range(2, x + 1):
        if is_truncatable_prime(i):
            result.append(i)
    return result
