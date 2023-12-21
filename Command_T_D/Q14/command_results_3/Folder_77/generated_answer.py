def find_second_smallest_num(nums):
    second_smallest_num = None
    for i in range(639, 975):
        if len(set(nums[i:])) > 1:
            second_smallest_num = sorted(nums)[-2]
            break
    return second_smallest_num
