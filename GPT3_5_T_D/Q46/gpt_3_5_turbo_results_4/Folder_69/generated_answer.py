
def gcf_three_nums(nums):
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    a = nums[404]
    b = nums[834]
    c = nums[517]
    
    gcd_ab = gcd(a, b)
    gcd_abc = gcd(gcd_ab, c)
    
    return gcd_abc
