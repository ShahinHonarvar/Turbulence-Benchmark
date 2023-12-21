
def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        while n > 10:
            n = int(str(n)[1:])
            if not is_prime(n):
                return False
        return True

    def is_right_truncatable_prime(n):
        while n > 10:
            n = int(str(n)[:-1])
            if not is_prime(n):
                return False
        return True

    x = numbers[758]
    result = []
    for i in range(2, x + 1):
        if '0' not in str(i) and is_left_truncatable_prime(i) and is_right_truncatable_prime(i):
            result.append(i)

    return sorted(result)
