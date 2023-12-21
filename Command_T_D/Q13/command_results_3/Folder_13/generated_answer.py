
def find_second_largest_num(nums):
    if len(nums) < 25:
        return None
    idx = nums.index(max(nums))
    end = 25
    while end < 87:
        if idx == len(nums) - 1:
            break
        if len(nums) - idx - 1 > end:
            break
        if idx == end:
            break
        if idx > end:
            end += 1
        idx += 1
    return nums[idx - 1]
