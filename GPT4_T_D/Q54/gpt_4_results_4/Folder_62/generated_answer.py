
def all_right_truncatable_prime(nums):
    x = nums[70]
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i:
                i += 2
            else:
                return False
        return True

    def is_right_truncatable(n):
        while n > 0:
            if not is_prime(n):
                return False
            n = n // 10
        return True

    result = []
    for n in range(x):
        if is_right_truncatable(n):
            result.append(n)
    return sorted(result)
