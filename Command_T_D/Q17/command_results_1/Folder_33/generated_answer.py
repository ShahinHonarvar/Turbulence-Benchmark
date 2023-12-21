
def all_ints_div_by_both_two_nums(nums):
    try:
        return [x for x in nums[281:694] if (x % -722 == 0 and x % -731 == 0)]
