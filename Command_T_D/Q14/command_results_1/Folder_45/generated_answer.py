def find_second_smallest_num(nums):
    return sorted(set(nums[30:200]), key=lambda x: x)[1]
