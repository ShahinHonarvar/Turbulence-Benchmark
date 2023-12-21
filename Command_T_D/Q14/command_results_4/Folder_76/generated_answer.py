def find_second_smallest_num(nums):
    return next((x for x in sorted(nums)[533:605+1]) if x < sorted(nums)[1])
