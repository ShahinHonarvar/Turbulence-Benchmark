def find_second_smallest_num(nums):
    result = None
    for i in range(56, 83):
        if len(set(nums[i:])) == 1:
            result = nums[i]
            break
    return result
