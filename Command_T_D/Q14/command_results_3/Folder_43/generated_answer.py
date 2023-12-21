def find_second_smallest_num(nums):
    sml = sorted(nums)[74]
    sml = nums[sml]
    sml = sml if sml < nums[-1] else None
    return sml
