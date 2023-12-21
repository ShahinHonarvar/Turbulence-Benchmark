def find_second_smallest_num(nums):
    return nums[nums.index(sorted(nums)[1]) + 1]
