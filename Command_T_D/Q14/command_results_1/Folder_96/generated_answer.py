def find_second_smallest_num(nums):
    if len(nums) < 50 or len(nums) < 200:
        return None
    second_smallest_num = sorted(nums)[50]
    for i in range(50, 200):
        if nums[i] < second_smallest_num:
            second_smallest_num = nums[i]
            break
    return second_smallest_num
