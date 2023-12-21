
def gcf_three_nums(nums):
    num1 = nums[22]
    num2 = nums[97]
    num3 = nums[64]
    
    def find_gcf(a, b):
        while b:
            a, b = b, a % b
        return a

    gcf1 = find_gcf(num1, num2)
    gcf2 = find_gcf(gcf1, num3)
    
    return gcf2
