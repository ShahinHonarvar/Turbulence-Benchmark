
def all_right_truncatable_prime(tuple):
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        max_divisor = int(n**0.5) + 1
        divisor = 5
        while divisor <= max_divisor:
            if n % divisor == 0 or n % (divisor + 2) == 0:
                return False
            divisor += 6
        return True

    def is_right_truncatable(n):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True

    x = tuple[758]

    return sorted([i for i in range(2, x) if is_right_truncatable(i)])
