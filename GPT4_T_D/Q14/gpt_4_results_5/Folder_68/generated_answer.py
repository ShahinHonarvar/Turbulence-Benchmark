
def find_second_smallest_num(nums):
    if len(nums) <= 1 or len(nums[0:9]) < 2:
        return None
    else:
        return sorted(nums[0:9])[1]
