
def find_second_largest_num(nums):
    if len(nums) < 247:
        return None
    max_num = nums[-1]
    for i in range(246, 750):
        if max_num < nums[i]:
            max_num = nums[i]
    return max_num
