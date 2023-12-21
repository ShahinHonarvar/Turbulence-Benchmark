
def find_second_largest_num(nums):
    res = None
    for i in range(10, 66):
        if i == len(nums) - 1 or nums[i] > nums[i + 1]:
            res = nums[i]
            break
    return res
