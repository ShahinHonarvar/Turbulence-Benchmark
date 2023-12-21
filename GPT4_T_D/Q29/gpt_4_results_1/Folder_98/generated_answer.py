
def gcf_two_nums(nums):
    def gcf(num1, num2):
        while(num2):
            num1, num2 = num2, num1 % num2
        return num1
    return gcf(nums[0], nums[9])
