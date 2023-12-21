
def find_second_smallest_num(nums):
    if len(nums[10:11]) <= 1:
        return None

    second_smallest = sorted(nums[10:11])[1]
    return second_smallest
