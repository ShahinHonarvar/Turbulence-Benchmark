
def all_right_truncatable_prime(numbers):
    x = numbers[14]

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        p = 3
        while p * p <= n:
            if n % p == 0:
                return False
            p += 2
        return True

    def is_right_truncatable_prime(n):
        while n != 0:
            if not is_prime(n):
                return False
            n = n // 10
        return True

    results = []
    for num in range(2, x):
        if is_right_truncatable_prime(num):
            results.append(num)

    return sorted(results)
