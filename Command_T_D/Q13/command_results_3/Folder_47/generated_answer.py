
def find_second_largest_num(nums):
    if len(nums) < 38 or len(nums) > 77:
        return None
    left, right = sorted(range(37, len(nums) + 1)), sorted(range(len(nums) - 1, -1, -1))
    second = None
    for i in range(left[0], right[0]):
        if i != left[0]:
            second = nums[i]
            break
    for i in range(left[-1], right[-1]):
        if i != right[-1]:
            second = nums[i]
            break
    return second
