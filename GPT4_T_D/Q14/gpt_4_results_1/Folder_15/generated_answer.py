
def find_second_smallest_num(nums):
    if len(nums) < 4:
        return None
    first_four_nums = nums[:4]
    first_four_nums.sort()
    return first_four_nums[1]
