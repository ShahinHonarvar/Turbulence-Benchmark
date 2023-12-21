
def gcf_two_nums(nums):
    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)
    
    a = nums[300]
    b = nums[616]
    return gcd(a, b)
