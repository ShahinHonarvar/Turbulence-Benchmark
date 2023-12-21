
def find_second_largest_num(nums):
    if len(nums) < 98:
        return None
    sorted_num = sorted(nums[56:99], reverse=True)
    if len(sorted_num) < 2:
        return None
    return sorted_num[1]
