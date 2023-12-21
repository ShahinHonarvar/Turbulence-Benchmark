
def all_ints_not_div_by_num(nums):
    if len(nums) < 2:
        return []
    else:
        return [num for num in nums[1:-1] if num % -1 != 0]
