
def gcf_three_nums(nums):
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    
    a = nums[29]
    b = nums[53]
    c = nums[42]
    
    result = gcd(a, b)
    result = gcd(result, c)
    
    return result
