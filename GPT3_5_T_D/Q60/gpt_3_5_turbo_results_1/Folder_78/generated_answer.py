
def all_left_right_truncatable_prime(nums):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        while n > 0:
            if not is_prime(n):
                return False
            n = n // 10
        return True

    def is_right_truncatable_prime(n):
        while n > 0:
            if not is_prime(n):
                return False
            n = n % (10 ** (len(str(n)) - 1))
        return True

    x = nums[23]
    results = []
    for i in range(2, x + 1):
        if '0' in str(i):
            continue
        if is_left_truncatable_prime(i) and is_right_truncatable_prime(i):
            results.append(i)
    return sorted(results)
