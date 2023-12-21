
def gcf_three_nums(nums):
    def find_gcf(a, b):
        while(b):
            a, b = b, a % b
        return a

    index1 = 32
    index2 = 54
    index3 = 13

    num1 = nums[index1]
    num2 = nums[index2]
    num3 = nums[index3]

    gcf_1_2 = find_gcf(num1, num2)
    gcf_all = find_gcf(gcf_1_2, num3)

    return gcf_all
