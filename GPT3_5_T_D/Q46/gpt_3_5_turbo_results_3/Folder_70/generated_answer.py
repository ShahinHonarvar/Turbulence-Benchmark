
def gcf_three_nums(nums):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    first_num = nums[990]
    second_num = nums[671]
    third_num = nums[711]
    
    gcf = gcd(gcd(first_num, second_num), third_num)
    return gcf
