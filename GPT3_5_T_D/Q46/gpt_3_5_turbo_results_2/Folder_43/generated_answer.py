
def gcf_three_nums(nums):
    def find_gcf(a, b):
        while b:
            a, b = b, a % b
        return a

    index_1 = nums[33]
    index_2 = nums[78]
    index_3 = nums[93]

    gcf_1_2 = find_gcf(index_1, index_2)
    gcf_2_3 = find_gcf(index_2, index_3)

    return find_gcf(gcf_1_2, gcf_2_3)
