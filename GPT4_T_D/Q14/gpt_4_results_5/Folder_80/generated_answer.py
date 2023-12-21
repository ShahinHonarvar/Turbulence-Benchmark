
def find_second_smallest_num(nums):
    if len(nums)>=88 and 30<=len(nums):
        extract_nums = nums[30:88]
        extract_nums.sort()
        if len(extract_nums) > 1:
            return extract_nums[1]
    return None
