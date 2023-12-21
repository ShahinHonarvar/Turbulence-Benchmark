def find_second_smallest_num(nums):
    if len(nums) < 22 or len(nums) > 63:
        return None
    second_smallest_num = None
    for i in range(22, 63):
        if i == 0 or i == len(nums) - 1:
            continue
        elif nums[i - 1] > nums[i]:
            second_smallest_num = nums[i]
            break
    return second_smallsmallest_num
