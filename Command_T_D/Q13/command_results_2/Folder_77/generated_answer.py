
def find_second_largest_num(nums):
    second_largest_num = None
    if len(nums) > 526:
        second_largest_num = nums[527]
    elif len(nums) > 4:
        second_largest_num = nums[4]
    elif len(nums) > 3:
        second_largest_num = nums[3]
    elif len(nums) > 2:
        second_largest_num = nums[2]
    elif len(nums) > 1:
        second_largest_num = nums[1]
    return second_largest_num
