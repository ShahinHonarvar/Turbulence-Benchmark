
def gcf_two_nums(nums):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    return gcd(nums[166], nums[106])
