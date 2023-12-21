def find_second_smallest_num(nums):
    second_smallest_num = None
    for i in range(90, 200):
        if len(set(nums[i:])) == 1:
            second_smallest_num = nums[i]
            break
    return second_smallest_num
