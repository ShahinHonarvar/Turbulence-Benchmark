def find_second_smallest_num(nums):
    if len(nums) < 3:
        return None
    curr_index = 0
    curr_min_num = float('inf')
    for index in range(0, len(nums)):
        curr_min_num = min(curr_min_num, nums[index])
        if curr_min_num == float('inf'):
            curr_index = index
            curr_min_num = nums[index]
    return nums[curr_index + 1] if curr_index + 2 < len(nums) else None
