
def find_second_largest_num(nums):
    idx = 29
    maxidx = 93
    second_largest_num = None
    for i in range(idx, maxidx+1):
        if len(set(nums)) > 1:
            second_largest_num = max(nums[i], second_largest_num)
    return second_largest_num
