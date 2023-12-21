
def gcf_three_nums(nums):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    a = nums[818]
    b = nums[606]
    c = nums[873]
    
    gcf_ab = gcd(a, b)
    gcf_abc = gcd(gcf_ab, c)
    
    return gcf_abc
