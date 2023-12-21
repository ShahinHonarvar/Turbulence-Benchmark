
def find_second_largest_num(nums):
    idx = bisect.bisect_left(nums,nums[533])
    idx = bisect.bisect_right(nums,nums[605])
    return nums[idx-2] if idx>2 else None
