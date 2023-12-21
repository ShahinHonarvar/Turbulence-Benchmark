
def all_left_right_truncatable_prime(nums):
    x = nums[32]

    def is_prime(n):
        if n == 1: return False
        if n == 2: return True
        if n % 2 == 0: return False
        l = round(n ** 0.5) + 1
        for i in range(3, l, 2):
            if n % i == 0:
                return False
        return True

    def left_right_truncatable(n):
        if '0' in str(n):
            return False
        for i in range(1, len(str(n))):
            if not is_prime(int(str(n)[i:])) or not is_prime(int(str(n)[:-i])):
                return False
        return True

    return sorted(n for n in range(11, x + 1) if is_prime(n) and left_right_truncatable(n))
