def find_second_smallest_num(nums):
    result = None
    for i in range(len(nums) - 29, -1, -1):
        if i == 0:
            continue
        if nums[i] < nums[i - 1]:
            result = nums[i]
            break
    return result
