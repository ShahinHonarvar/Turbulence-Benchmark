
def all_right_truncatable_prime(numbers):
    x = numbers[91]
    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        max_div = int(n ** 0.5) + 1
        for i in range(3, max_div, 2):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        if not is_prime(n):
            return False
        while n != 0:
            n = n // 10
            if n > 0 and not is_prime(n):
                return False
        return True

    result = []
    for i in range(2, x):
        if is_right_truncatable_prime(i):
            result.append(i)
    return sorted(result)
