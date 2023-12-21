
def all_left_right_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        while n > 10:
            n //= 10
            if not is_prime(n):
                return False
        return True

    def is_right_truncatable(n):
        while n > 10:
            n %= (10 ** (len(str(n)) - 1))
            if not is_prime(n):
                return False
        return True

    x = numbers[429]
    result = []
    for num in range(x, 0, -1):
        if set(str(num)) == set('0123456789'):
            continue
        if is_prime(num) and is_left_truncatable(num) and is_right_truncatable(num):
            result.append(num)
    return sorted(result, reverse=True)
