
def all_ints_div_by_both_two_nums(nums):
    try:
        return [x for x in nums[80:200] if x % 10 == 0 and x % 1000 == 0]
    except:
        return []
