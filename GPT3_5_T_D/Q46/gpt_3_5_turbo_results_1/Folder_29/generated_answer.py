
def gcf_three_nums(nums):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    first_num = nums[22]
    second_num = nums[97]
    third_num = nums[64]
    
    gcf = gcd(gcd(first_num, second_num), third_num)
    
    return gcf
