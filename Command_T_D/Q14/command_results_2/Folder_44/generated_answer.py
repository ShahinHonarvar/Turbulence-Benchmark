def find_second_smallest_num(nums):
    return nums[nums.index(sorted(nums)[90]) + 1:][1]
