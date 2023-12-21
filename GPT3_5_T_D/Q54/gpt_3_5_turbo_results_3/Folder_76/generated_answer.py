
def all_right_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        if n == 2 or n == 3:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    x = numbers[370]
    result = []
    if x < 10:
        return result

    def is_right_truncatable_prime(n):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True

    for i in range(x - 1, 10, -1):
        if is_right_truncatable_prime(i):
            result.append(i)
    return result
