
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[64]
    result = []

    def is_right_truncatable_prime(num):
        if not is_prime(num):
            return False
        while num > 10:
            num //= 10
            if not is_prime(num):
                return False
        return True

    for i in range(x-1, 1, -1):
        if is_right_truncatable_prime(i):
            result.append(i)

    return sorted(result, reverse=True)
