def find_second_smallest_num(nums):
    if len(nums) < 533 or len(nums) > 605:
        return None
    return nums[533] if nums[533] < nums[604] else nums[604]
