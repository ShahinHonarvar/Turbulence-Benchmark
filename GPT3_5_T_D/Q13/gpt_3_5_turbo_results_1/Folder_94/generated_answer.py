
def find_second_largest_num(nums):
    nums.sort()
    if len(nums) < 29:
        return None
    return nums[-2]
