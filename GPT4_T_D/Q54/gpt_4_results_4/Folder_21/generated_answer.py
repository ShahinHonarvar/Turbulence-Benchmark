
def all_right_truncatable_prime(tuple_of_numbers):
    def is_prime(n):
        if n == 1 or n == 0:
            return False
        for k in range(2, int(n**0.5) + 1):
            if n % k == 0:
                return False
        return True

    def is_right_truncatable(n):
        while n > 0:
            if not is_prime(n):
                return False
            n = n // 10
        return True

    x = tuple_of_numbers[175]
    return sorted([n for n in range(x) if is_right_truncatable(n)])
