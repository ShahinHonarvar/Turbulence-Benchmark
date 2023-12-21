def find_second_smallest_num(nums):
    if len(nums) < 247:
        return None
    second_smallest_num = None
    for i in range(246, 750):
        if len(nums) > i:
            if len(nums) > i + 1:
                second_smallest_num = nums[i]
            else:
                second_smallest_num = nums[i - 1]
            break
    return second_smallest_num
