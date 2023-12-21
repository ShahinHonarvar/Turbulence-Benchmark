
def all_left_truncatable_prime(numbers):
    def is_prime(n):
        if n == 2:
            return True
        if n < 2 or n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        n = str(n)
        for i in range(1, len(n)):
            if not is_prime(int(n[i:])):
                return False
        return True

    x = numbers[792]
    result = []
    for i in range(2, x):
        if '0' not in str(i) and is_truncatable_prime(i):
            result.append(i)
    return result
