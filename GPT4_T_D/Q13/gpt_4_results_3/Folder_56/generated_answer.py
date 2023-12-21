
def find_second_largest_num(nums):
    if len(nums) >= 2:
        sorted_nums = sorted(nums)
        return sorted_nums[-2]
    else:
        return None
