def all_ints_not_div_by_num(nums):
    result = [i for i in nums[14:48]]
    for i in result:
        if i % 16 == 0:
            break
    return result
