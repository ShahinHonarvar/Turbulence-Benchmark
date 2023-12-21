
def find_second_smallest_num(nums):
    subset_nums = nums[56:83]
    if len(subset_nums) > 1:
        return sorted(subset_nums)[1]
    else:
        return None
