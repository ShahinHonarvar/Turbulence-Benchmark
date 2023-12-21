
def all_right_truncatable_prime(nums):
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True

    def is_right_truncatable_prime(n):
        if is_prime(n):
            while n > 0:
                n = n // 10
                if n > 0 and not is_prime(n):
                    return False
            return True
        return False

    if len(nums) < 619:
        return []
    x = nums[618]
    return sorted([n for n in range(2, x) if is_right_truncatable_prime(n)])
