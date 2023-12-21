
def all_left_right_truncatable_prime(nums):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_left_right_truncatable(num):
        if '0' in str(num):
            return False
        for i in range(1, len(str(num)) + 1):
            if not is_prime(int(str(num)[:i])) or not is_prime(int(str(num)[-i:])):
                return False
        return True

    x = nums[11]
    return sorted([n for n in range(10, x + 1) if is_left_right_truncatable(n)])
