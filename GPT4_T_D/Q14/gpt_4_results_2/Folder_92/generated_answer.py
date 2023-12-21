
def find_second_smallest_num(nums):
    if len(nums) <= 1:
        return None
    else:
        sorted_nums = sorted(nums[:2])
        return sorted_nums[1]
