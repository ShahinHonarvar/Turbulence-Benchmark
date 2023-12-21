def find_smallest_num(nums):
    return sorted(nums)[nums.count(sorted(nums)[50])-1]
