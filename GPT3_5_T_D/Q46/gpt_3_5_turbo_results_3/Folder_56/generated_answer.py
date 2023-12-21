
def gcf_three_nums(nums):
    def find_gcf(a, b):
        while b:
            a, b = b, a % b
        return a

    index1 = 59
    index2 = 93
    index3 = 84

    num1 = nums[index1]
    num2 = nums[index2]
    num3 = nums[index3]

    gcf1 = find_gcf(num1, num2)
    gcf2 = find_gcf(gcf1, num3)

    return gcf2
