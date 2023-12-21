
def all_right_truncatable_prime(nums):
    def is_prime(n):
        if n == 1 or n == 0:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        while n > 0:
            if not is_prime(n):
                return False
            n = n // 10
        return True

    x = nums[29]
    truncatable_prime_nums = [i for i in range(x) if is_right_truncatable_prime(i)]
    return sorted(truncatable_prime_nums, reverse=True)
