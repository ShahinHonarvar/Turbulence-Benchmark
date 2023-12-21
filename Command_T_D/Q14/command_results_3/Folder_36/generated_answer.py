def find_second_smallest_num(nums):
    return nums[ 209:556].index(sorted(set(nums[209:556]))[-2])
