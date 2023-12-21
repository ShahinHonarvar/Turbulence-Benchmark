
def find_second_largest_num(nums):
    nums = nums[27:56]
    if len(nums) < 2:
        return None
    let = sorted(nums)
    return let[-2]
