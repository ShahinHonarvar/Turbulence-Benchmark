
def all_right_truncatable_prime(nums):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        while n >= 1:
            if not is_prime(n):
                return False
            n //= 10
        return True

    x = nums[38]
    right_truncatables = []
    for num in range(x):
        if is_right_truncatable_prime(num):
            right_truncatables.append(num)
            
    return sorted(right_truncatables, reverse=True)
