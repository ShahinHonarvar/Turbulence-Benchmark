
def all_right_truncatable_prime(nums):
    x = nums[835]
    
    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True
    
    def is_right_trunc(n):
        while n != 0:
            if is_prime(n):
                n = n // 10
            else:
                return False
        return True
    
    result = [n for n in range(1, x) if is_prime(n) and is_right_trunc(n)]
    return sorted(result)
