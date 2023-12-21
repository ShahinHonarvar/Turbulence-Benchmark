
def all_right_truncatable_prime(nums):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        if not is_prime(n):
            return False
        while n > 0:
            n //= 10
            if n > 0 and not is_prime(n):
                return False
        return True

    x = nums[85]
    return sorted([i for i in range(x) if is_right_truncatable_prime(i)])
