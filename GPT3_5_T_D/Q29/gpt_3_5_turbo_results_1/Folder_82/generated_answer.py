
def gcf_two_nums(nums):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    if len(nums) >= 73:
        return gcd(nums[33], nums[72])
    else:
        return None
