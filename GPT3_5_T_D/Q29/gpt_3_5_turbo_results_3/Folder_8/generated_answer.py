
def gcf_two_nums(nums):
    def gcf(a, b):
        while b:
            a, b = b, a % b
        return a

    num1 = nums[69]
    num2 = nums[41]
    return gcf(num1, num2)
