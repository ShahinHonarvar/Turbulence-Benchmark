
def all_right_truncatable_prime(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    x = numbers[8]
    result = []

    def truncate_prime(n):
        if n < 10:
            return is_prime(n)
        if not is_prime(n):
            return False
        return truncate_prime(int(str(n)[:-1]))

    for i in range(2, x):
        if truncate_prime(i):
            result.append(i)

    result.sort(reverse=True)
    return result
