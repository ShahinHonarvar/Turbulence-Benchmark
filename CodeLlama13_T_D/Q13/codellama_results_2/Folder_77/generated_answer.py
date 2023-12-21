
def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    second_largest = sorted(nums)[-2]
    for i in range(527, 539):
        if nums[i] == second_largest:
            return second_largest
    return None
