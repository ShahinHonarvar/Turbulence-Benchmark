
def all_right_truncatable_prime(numbers):
    x = numbers[88]

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        max_divisor = round(n ** 0.5)
        for d in range(3, 1 + max_divisor, 2):
            if n % d == 0:
                return False
        return True

    def is_right_truncatable(n):
        n_str = str(n)
        for i in range(len(n_str)):
            if not is_prime(int(n_str[i:])):
                return False
        return True

    return sorted([n for n in range(x) if is_right_truncatable(n)])
