
def find_second_largest_num(nums):
    try:
        nums = nums[1:9]
        nums.remove(max(nums))
        return max(nums)
    except ValueError:
        return None
