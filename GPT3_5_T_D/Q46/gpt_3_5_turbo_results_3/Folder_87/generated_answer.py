
def gcf_three_nums(nums):
    def find_gcf(a, b):
        while b:
            a, b = b, a % b
        return a

    num1 = nums[74]
    num2 = nums[60]
    num3 = nums[28]
    gcf = find_gcf(find_gcf(num1, num2), num3)
    return gcf
