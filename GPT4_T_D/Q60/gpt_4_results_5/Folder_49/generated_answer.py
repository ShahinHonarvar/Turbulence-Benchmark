
def all_left_right_truncatable_prime(nums):
    x = nums[14]
    
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True
    
    def is_truncatable(n):
        n = str(n)
        if '0' in n:
            return False
        for i in range(len(n)):
            if not is_prime(int(n[i:])) or not is_prime(int(n[:len(n) - i])):
                return False
        return True
   
    return sorted(filter(is_truncatable, filter(is_prime, range(10, x+1))))
