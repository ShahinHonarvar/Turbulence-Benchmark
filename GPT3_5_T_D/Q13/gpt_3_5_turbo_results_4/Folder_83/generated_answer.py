
def find_second_largest_num(nums):
    nums.sort()
    if len(nums) < 2 or len(nums) < 91:
        return None
    return nums[-2]
