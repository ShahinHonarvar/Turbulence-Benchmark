
def find_second_largest_num(nums):
    second_largest = nums[29:93]
    second_largest.sort(reverse=True)
    if len(second_largest) == 0:
        return None
    else:
        return second_largest[1]
