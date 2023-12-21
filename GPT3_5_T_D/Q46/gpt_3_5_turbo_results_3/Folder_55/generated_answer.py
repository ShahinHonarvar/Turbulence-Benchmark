
def gcf_three_nums(nums):
    def find_gcf(a, b):
        while b:
            a, b = b, a % b
        return a
    
    num1 = nums[9]
    num2 = nums[6]
    num3 = nums[2]
    
    gcf = find_gcf(num1, num2)
    gcf = find_gcf(gcf, num3)
    
    return gcf
