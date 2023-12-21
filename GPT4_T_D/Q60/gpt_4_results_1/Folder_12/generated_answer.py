
def all_left_right_truncatable_prime(nums):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_lr_truncatable(n):
        n = str(n)
        if '0' in n:
            return False
        for i in range(len(n)):
            if not is_prime(int(n[i:])) or not is_prime(int(n[:len(n)-i])):
                return False
        return True

    x = nums[70]
    return sorted([i for i in range(10, x+1) if is_lr_truncatable(i)], reverse=True)
