
def all_left_right_truncatable_prime(nums):
    x = nums[0]

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        if not is_prime(n) or '0' in str(n):
            return False
        for i in range(1, len(str(n))):
            if not is_prime(int(str(n)[i:])) or not is_prime(int(str(n)[:i])):
                return False
        return True

    return sorted([i for i in range(x, 10, -1) if is_truncatable(i)], reverse=True)
