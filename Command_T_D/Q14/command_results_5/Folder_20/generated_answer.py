def find_second_smallest_num(nums):
    return nums[nums.index(sorted(nums)[75:94]) - 1]
