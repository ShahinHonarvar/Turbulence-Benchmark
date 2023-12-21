
def gcf_three_nums(nums):
    index_1 = 67
    index_2 = 84
    index_3 = 13

    def find_gcf(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    num_1 = nums[index_1]
    num_2 = nums[index_2]
    num_3 = nums[index_3]

    gcf = find_gcf(num_1, num_2)
    gcf = find_gcf(gcf, num_3)

    return gcf
