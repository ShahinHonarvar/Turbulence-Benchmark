
def all_left_truncatable_prime(numbers):
    def is_prime(n):
        if n in [2, 3]:
            return True
        if n == 1 or n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        while n > 0:
            if not is_prime(n):
                return False
            n = int(str(n)[1:])
        return True

    x = numbers[31]
    result = [num for num in range(x-1, 1, -1) if is_left_truncatable_prime(num)]
    return sorted(result, reverse=True)
