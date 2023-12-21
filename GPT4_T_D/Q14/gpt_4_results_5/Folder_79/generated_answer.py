
def find_second_smallest_num(nums):
    try:
        sorted_nums = sorted(nums[1:6])
        if len(sorted_nums) > 1:
            return sorted_nums[1]
        else:
            return None
    except IndexError:
        return None
