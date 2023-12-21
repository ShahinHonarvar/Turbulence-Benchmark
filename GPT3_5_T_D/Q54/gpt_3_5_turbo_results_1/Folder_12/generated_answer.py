
def all_right_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        if not is_prime(n):
            return False
        while n > 10:
            n = int(str(n)[:-1])
            if not is_prime(n):
                return False
        return True

    x = numbers[70]
    result = []
    for i in range(x - 1, 10, -1):
        if is_right_truncatable_prime(i):
            result.append(i)
    return sorted(result, reverse=True)
