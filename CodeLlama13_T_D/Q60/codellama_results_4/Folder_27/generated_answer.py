
def all_left_right_truncatable_prime(nums):
    def is_prime(n):
        if n < 2: return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0: return False
        return True

    def is_truncatable_prime(n):
        if not is_prime(n): return False
        for i in range(len(str(n)) - 2, 0, -1):
            if not is_prime(int(str(n)[:i])): return False
        return True

    return sorted([n for n in nums if is_truncatable_prime(n)], reverse=True)
