def find_second_smallest_num(nums):
    result = next((x for x in sorted(set(range(31, 73)))(nums), key=lambda x: nums.count(x)) if x != nums[30] and x != nums[71]), None)
    return result
