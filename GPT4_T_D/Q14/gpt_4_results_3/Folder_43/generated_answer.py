
def find_second_smallest_num(nums):
    try:
        subset = sorted(nums[74:96])
        return subset[1]
    except IndexError:
        return None
