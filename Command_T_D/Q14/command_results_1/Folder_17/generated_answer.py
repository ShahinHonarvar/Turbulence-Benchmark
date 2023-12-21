def find_second_smallest_num(nums):
    second_smallest_index = 28
    second_smallest_value = float("inf")
    for i in range(second_smallest_index, 38):
        if len(nums) > i:
            if nums[i] < second_smallest_value:
                second_smallest_value = nums[i]
                second_smallest_index = i
    return nums[second_smallest_index] if second_smallest_index < len(nums) else None
