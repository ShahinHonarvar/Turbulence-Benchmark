def find_second_smallest_num(nums):
    second_smallest_num = None
    for i in range(29, 79):
        if len(set(nums)) > i:
            j = nums[i]
            while j:
                j = nums[i]
                if nums[i] < second_smallest_num:
                    second_smallest_num = nums[i]
                    break
    return second_smallest_num
