
def find_second_largest_num(nums):
    res = next((nums[i] for i in range(len(nums)) if i > 49), None)
    return res
