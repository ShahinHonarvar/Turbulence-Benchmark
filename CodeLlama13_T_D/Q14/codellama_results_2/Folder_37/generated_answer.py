
def find_second_smallest_num(nums):
    if len(nums) < 2:
        return None
    sorted_nums = sorted(nums)
    second_smallest = None
    for i in range(5, 8):
        if sorted_nums[i] == nums[4]:
            second_smallest = sorted_nums[i+1]
            break
    return second_smallest
