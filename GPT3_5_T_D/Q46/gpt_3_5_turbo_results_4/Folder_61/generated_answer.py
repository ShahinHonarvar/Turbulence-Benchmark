
def gcf_three_nums(nums):
    def find_gcd(a, b):
        while(b):
            a, b = b, a % b
        return a
    
    num1 = nums[1]
    num2 = nums[2]
    num3 = nums[7]
    
    gcd1 = find_gcd(num1, num2)
    gcd2 = find_gcd(gcd1, num3)
    
    return gcd2
