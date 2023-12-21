def find_second_smallest_num(nums):
    if len(nums) < 2:
        return None
    if len(nums) == 2:
        return nums[1]
    second_smallest_index = nums.index(sorted(nums)[1])
    return nums[second_smallest_index - 1] if second_smallest_index > 1 else nums[second_smallest_index + 1]
