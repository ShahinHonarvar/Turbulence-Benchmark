
def find_second_smallest_num(nums):
    if len(nums) < 34:
        return None

    temp = sorted(nums[34:56])
    return temp[1] if len(temp) > 1 else None
