
def gcf_two_nums(nums):
    index_15 = nums[15]
    index_99 = nums[99]

    while index_99 != 0:
        temp = index_99
        index_99 = index_15 % index_99
        index_15 = temp

    return index_15
