
def all_left_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(num):
        while num > 0:
            if not is_prime(num):
                return False
            num //= 10
        return True

    x = numbers[0]
    result = []
    for i in range(x - 1, 0, -1):
        if '0' not in str(i) and is_left_truncatable_prime(i):
            result.append(i)
    return result
