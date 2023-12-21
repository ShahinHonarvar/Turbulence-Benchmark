
def sum_ints_div_by_either_nums(nums):
    if len(nums) < 281 or len(nums) > 694:
        return 0
    if nums[280] % -722 != 0 and nums[694] % -722 != 0:
        return 0
    if nums[281] % -731 != 0 and nums[694] % -731 != 0:
        return 0
    return sum(nums[ 281 : 694 + 1])
