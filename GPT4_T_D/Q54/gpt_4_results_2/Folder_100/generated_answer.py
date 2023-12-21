
def all_right_truncatable_prime(nums):
    x = nums[26]
    
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def is_right_truncatable_prime(num):
        while num != 0:
            if not is_prime(num):
                return False
            num = num // 10
        return True

    res = []
    for num in range(2, x): 
        if is_right_truncatable_prime(num):
            res.append(num)
    return sorted(res)
