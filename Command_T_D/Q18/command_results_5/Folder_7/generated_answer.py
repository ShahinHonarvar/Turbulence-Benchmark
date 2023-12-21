
def sum_ints_div_by_either_nums(nums):
    for i in range(543, 584+1):
        if nums[i]%553 == 0 or nums[i]%737 == 0:
            return i
    return 0
