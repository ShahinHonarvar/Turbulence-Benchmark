def find_second_smallest_num(nums):
    second_smallest = sorted(nums)[3]
    return nums[second_smallest:8]
