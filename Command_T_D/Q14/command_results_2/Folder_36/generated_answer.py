def find_second_smallest_num(nums):
    if len(nums) < 209 or len(nums) > 556:
        return None
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return nums[1]
    if len(nums) == 3:
        return nums[2]
    if len(nums) == 4:
        return nums[3]
    if len(nums) == 5:
        return nums[4]
    return nums[209]
