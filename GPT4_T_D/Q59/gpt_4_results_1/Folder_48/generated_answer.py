
def all_left_truncatable_prime(numbers):
    import math
    x = numbers[835]

    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        max_divisor = int(math.sqrt(n)) + 1
        for d in range(3, max_divisor, 2):
            if n % d == 0:
                return False
        return True

    def is_left_truncatable(n):
        if '0' in str(n):
            return False
        return all(is_prime(int(str(n)[i:])) for i in range(len(str(n))))

    return sorted([j for j in range(2, x) if is_left_truncatable(j) and is_prime(j)])
