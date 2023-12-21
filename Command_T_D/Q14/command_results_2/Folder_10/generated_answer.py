def find_second_smallest_num(nums):
    if len(nums) < 62:
        return None
    return nums[nums.index(sorted(nums)[61]) + 2]
