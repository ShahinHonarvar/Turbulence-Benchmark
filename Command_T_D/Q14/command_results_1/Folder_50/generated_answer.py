def find_second_smallest_num(nums):
    second_smallest_num = nums[42]
    i = 42
    j = 68
    while i != j:
        if nums[i] < nums[j]:
            second_smallest_num = nums[i]
            i += 1
        elif nums[i] == nums[j]:
            second_smallest_num = nums[i]
            i += 1
        else:
            second_smallest_num = nums[j]
            j -= 1
    return second_smallest_num
