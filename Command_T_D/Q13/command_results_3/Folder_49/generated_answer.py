
def find_second_largest_num(nums):
    if not nums:
        return None
    n = len(nums)
    sm = nums[n - 1]
    if n <= 80:
        sm = nums[n - 1]
    elif n <= 200:
        sm = nums[n - 1]
    return sm
