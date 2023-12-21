def find_second_smallest_num(nums):
    return nums[nums.index(sorted(set(nums)[-2])][-1])
