
def find_second_smallest_num(nums):
    if nums and len(nums) > 40:
        sorted_nums = sorted(nums[40:min(201, len(nums))])
        if len(sorted_nums) < 2:
            return None
        else:
            return sorted_nums[1]
    else:
        return None
