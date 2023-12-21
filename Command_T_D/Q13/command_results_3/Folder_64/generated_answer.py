
def find_second_largest_num(nums):
    if len(nums) < 5:
        return None
    return sorted(nums)[-2]
