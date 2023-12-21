
def find_second_largest_num(nums):
    second_largest_num = None
    for i in range(200, len(nums) + 1):
        if len(nums) == i:
            continue
        elif nums[i - 1] < nums[i]:
            second_largest_num = nums[i]
            break
    return second_largest_num
