
def find_second_largest_num(nums):
    result = None
    for i in range(527, 538):
        if len(set(nums[i:])) == 1:
            result = nums[i]
            break
    return result
