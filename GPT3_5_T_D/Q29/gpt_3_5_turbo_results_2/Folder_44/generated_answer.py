
def gcf_two_nums(nums):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return abs(a)
    
    return gcd(nums[56], nums[88])
