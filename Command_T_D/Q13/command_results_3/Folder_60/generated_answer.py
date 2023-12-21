
def find_second_largest_num(nums):
    second_largest_num = None
    second_largest_idx = 75
    largest_idx = 85
    largest_num = None
    for i in range(len(nums)):
        if i == second_largest_idx:
            second_largest_num = nums[i]
        elif i == largest_idx:
            largest_num = nums[i]
        elif nums[i] > largest_num:
            second_largest_num = largest_num
            largest_num = nums[i]
            second_largest_idx = largest_idx
            largest_idx = i
    return second_largest_num
