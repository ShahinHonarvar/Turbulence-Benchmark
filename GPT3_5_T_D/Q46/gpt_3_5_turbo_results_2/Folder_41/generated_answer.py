
def gcf_three_nums(nums):
    def find_gcf(a, b):
        while b != 0:
            (a, b) = (b, a % b)
        return a

    num1 = nums[19]
    num2 = nums[94]
    num3 = nums[78]

    gcf1 = find_gcf(num1, num2)
    gcf2 = find_gcf(gcf1, num3)

    return gcf2
