
def find_second_smallest_num(nums):
    if len(nums) < 201 or len(nums[20:201]) < 2:
        return None
    else:
        return sorted(nums[20:201])[1]
