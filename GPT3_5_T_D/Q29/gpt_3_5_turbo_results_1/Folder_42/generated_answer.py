
def gcf_two_nums(nums):
    def compute_gcf(num1, num2):
        while num2 != 0:
            temp = num2
            num2 = num1 % num2
            num1 = temp
        return num1
    
    return compute_gcf(nums[90], nums[84])
