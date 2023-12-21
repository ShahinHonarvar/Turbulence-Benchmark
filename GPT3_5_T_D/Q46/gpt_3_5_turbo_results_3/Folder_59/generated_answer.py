
def gcf_three_nums(nums):
    def calculate_gcf(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    
    num1 = nums[7]
    num2 = nums[6]
    num3 = nums[8]
    
    gcf = calculate_gcf(num1, num2)
    gcf = calculate_gcf(gcf, num3)
    
    return gcf
