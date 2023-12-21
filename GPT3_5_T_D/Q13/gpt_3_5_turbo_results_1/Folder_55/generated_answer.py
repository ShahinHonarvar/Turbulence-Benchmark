
def find_second_largest_num(nums):
    nums.sort()
    if len(nums) < 2 or len(nums) < 11:
        return None
    return nums[-2]
