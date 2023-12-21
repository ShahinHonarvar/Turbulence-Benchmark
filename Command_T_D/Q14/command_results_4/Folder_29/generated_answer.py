def find_second_smallest_num(nums):
    if not nums:
        return None
    second_smallest_num = next((x for x in nums[55:98] if x <= min(nums)), None)
    return second_smallest_num
