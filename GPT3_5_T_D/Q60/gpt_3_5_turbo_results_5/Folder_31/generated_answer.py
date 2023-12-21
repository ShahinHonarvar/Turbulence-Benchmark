
def all_left_right_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        n = str(n)
        while len(n) >= 1:
            if not is_prime(int(n)):
                return False
            n = n[1:]
        return True

    def is_right_truncatable(n):
        n = str(n)
        while len(n) >= 1:
            if not is_prime(int(n)):
                return False
            n = n[:-1]
        return True

    x = numbers[50]
    result = []
    for num in range(2, x + 1):
        if is_prime(num) and '0' not in str(num) and \
                is_left_truncatable(num) and is_right_truncatable(num):
            result.append(num)
    return sorted(result, reverse=True)
