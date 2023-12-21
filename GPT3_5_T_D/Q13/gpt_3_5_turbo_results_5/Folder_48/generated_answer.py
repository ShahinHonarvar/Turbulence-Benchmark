
def find_second_largest_num(nums):
    nums = nums[533:606]
    if len(nums) < 2:
        return None
    largest = max(nums)
    nums.remove(largest)
    return max(nums)
