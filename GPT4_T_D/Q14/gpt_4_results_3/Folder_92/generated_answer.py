
def find_second_smallest_num(nums):
    if len(nums) >= 2:
        sorted_nums = sorted(nums[:2])
        return sorted_nums[1]
    else:
        return None
