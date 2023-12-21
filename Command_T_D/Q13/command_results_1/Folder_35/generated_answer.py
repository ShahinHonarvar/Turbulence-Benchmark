
def find_second_largest_num(nums):
    if len(nums) < 30 or len(nums) > 48:
        return None
    a = nums[30]
    b = nums[31]
    for i in range(32, 48):
        if nums[i] > b:
            b = nums[i]
        elif nums[i] == b:
            a = nums[i]
    return a if a != b else b
