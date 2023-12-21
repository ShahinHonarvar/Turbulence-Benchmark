
def all_ints_div_by_both_two_nums(nums):
    result = []
    for i in range(543, 584):
        if nums[i] % -553 == nums[i] % -737:
            result.append(nums[i])
    return result
