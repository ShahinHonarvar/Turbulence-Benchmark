
def find_second_smallest_num(nums):
    if len(nums) < 88:
        return None
    else:
        seq = sorted(nums[25:88])
        if len(seq) > 1:
            return seq[1]
        else:
            return None
