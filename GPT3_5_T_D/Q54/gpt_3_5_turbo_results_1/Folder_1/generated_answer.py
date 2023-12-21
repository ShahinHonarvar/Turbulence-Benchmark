
def all_right_truncatable_prime(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    x = numbers[20]
    result = []

    def check_truncatable_prime(num):
        if num == 0:
            return True
        if not is_prime(num):
            return False
        return check_truncatable_prime(num // 10)

    for i in range(x-1, 1, -1):
        if check_truncatable_prime(i):
            result.append(i)

    return sorted(result, reverse=True)
