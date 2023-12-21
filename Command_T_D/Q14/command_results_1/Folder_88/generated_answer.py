def find_second_smallest_num(nums):
    sml_nums = sorted(nums)[6:8]
    if len(sml_nums) < 2:
        return None
    return sml_nums[1]
