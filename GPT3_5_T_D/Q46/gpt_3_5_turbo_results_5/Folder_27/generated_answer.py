
def gcf_three_nums(nums):
    def find_gcd(x, y):
        while(y):
            x, y = y, x % y
        return x
    
    num1 = nums[76]
    num2 = nums[64]
    num3 = nums[28]
    
    gcd1 = find_gcd(num1, num2)
    gcd2 = find_gcd(gcd1, num3)
    
    return gcd2
