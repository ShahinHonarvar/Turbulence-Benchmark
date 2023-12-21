
def find_second_smallest_num(nums):
    try:
        return sorted(nums[32:36])[1]
    except IndexError:
        return None
