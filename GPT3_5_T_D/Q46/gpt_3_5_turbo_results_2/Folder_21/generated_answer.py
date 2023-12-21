
def gcf_three_nums(nums):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    a = nums[412]
    b = nums[932]
    c = nums[337]
    
    gcf_ab = gcd(a, b)
    gcf_abc = gcd(gcf_ab, c)
    
    return gcf_abc
