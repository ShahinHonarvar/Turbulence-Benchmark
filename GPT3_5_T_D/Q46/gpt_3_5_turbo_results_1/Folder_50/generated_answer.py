
def gcf_three_nums(nums):
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a
        
    a = nums[20]
    b = nums[35]
    c = nums[74]
    
    result = gcd(a, gcd(b, c))
    return result
