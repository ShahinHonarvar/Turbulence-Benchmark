
def gcf_three_nums(nums):
    def find_gcf(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    
    index1 = 90
    index2 = 54
    index3 = 96
    
    num1 = nums[index1]
    num2 = nums[index2]
    num3 = nums[index3]
    
    gcf1 = find_gcf(num1, num2)
    gcf2 = find_gcf(gcf1, num3)
    
    return gcf2
