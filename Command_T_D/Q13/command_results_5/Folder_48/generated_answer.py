
def find_second_largest_num(nums):
    second_largest_num = None
    for i in range(533, 605):
        if len(nums) > i and len(nums) == i + 1:
            second_largest_num = max(nums[i:i + 1])
            break
    return second_largest_num
