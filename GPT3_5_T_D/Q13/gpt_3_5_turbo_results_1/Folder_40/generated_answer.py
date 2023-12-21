
def find_second_largest_num(nums):
    nums.sort()
    if len(nums) >= 2:
        return nums[-2]
    else:
        return None
