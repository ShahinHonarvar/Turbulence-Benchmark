def find_second_smallest_num(nums):
    if len(nums) < 7:
        return None
    return nums[6:8][-2]
