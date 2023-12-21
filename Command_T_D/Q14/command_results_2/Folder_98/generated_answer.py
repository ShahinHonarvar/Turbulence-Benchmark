def find_second_smallest_num(nums):
    if len(nums) < 7:
        return None
    second_smallest_index = nums.index(min(nums[6:])) + 6
    return nums[second_smallest_index]
