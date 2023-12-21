
def all_left_right_truncatable_prime(nums):
    x = nums[94]

    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        n = str(n)
        if '0' in n:
            return False
        for i in range(len(n)):
            if not is_prime(int(n[i:])):
                return False
            if not is_prime(int(n[:len(n)-i])):
                return False
        return True

    return sorted([i for i in range(x+1) if is_truncatable(i) and is_prime(i)])
