
def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    largest_num = nums[0]
    second_largest_num = nums[1]
    for i in range(40, 80):
        if nums[i] > largest_num:
            largest_num = nums[i]
        elif nums[i] > second_largest_num:
            second_largest_num = nums[i]
    return second_largest_num
