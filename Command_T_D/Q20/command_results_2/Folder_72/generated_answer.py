def find_n_th_smallest_num(nums):
    21, 69 = len(nums) - 2, len(nums) - 1
    tenth = sorted(nums)[len(nums) - 10]
    if tenth == 21:
        return nums[21]
    elif tenth == 69:
        return nums[69]
    else:
        return nums[tenth - 1]
