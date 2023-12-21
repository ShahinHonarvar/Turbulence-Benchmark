
def all_left_right_truncatable_prime(numbers):
    def is_prime(n):
        if n in (2, 3):
            return True
        if n == 1 or n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        if '0' in str(n):
            return False
        while n > 10:
            if not is_prime(n):
                return False
            n = n // 10
        return is_prime(n)

    x = numbers[91]
    result = []
    for num in range(2, x + 1):
        if is_truncatable_prime(num):
            result.append(num)
    return sorted(result)
