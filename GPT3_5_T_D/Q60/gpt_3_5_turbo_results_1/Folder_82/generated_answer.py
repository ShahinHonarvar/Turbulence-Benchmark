
def all_left_right_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(n):
        for i in range(1, len(str(n))):
            left_trunc = int(str(n)[i:])
            right_trunc = int(str(n)[:i])
            if not is_prime(left_trunc) or not is_prime(right_trunc):
                return False
        return True

    x = numbers[69]
    result = []
    for num in range(2, x + 1):
        if '0' not in str(num) and is_left_right_truncatable_prime(num):
            result.append(num)
    return sorted(result, reverse=True)
