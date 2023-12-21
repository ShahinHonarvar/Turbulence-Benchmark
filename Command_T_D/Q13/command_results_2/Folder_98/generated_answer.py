
def find_second_largest_num(nums):
    second_largest_num = None
    for i in range(len(nums)):
        if i == 0:
            continue
        elif i == len(nums) - 1:
            continue
        elif nums[i] > second_largest_num:
            second_largest_num = nums[i]
    return second_largest_num
