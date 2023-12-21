
def all_left_right_truncatable_prime(nums):
    from sympy import isprime
    
    def is_left_right_truncatable(num):
        s = str(num)
        return all(isprime(int(s[i:len(s)-i])) for i in range(len(s)))
    
    x = nums[100]
    return sorted(num for num in range(10, x+1) if '0' not in str(num) and isprime(num) and is_left_right_truncatable(num))
