
def find_second_smallest_num(nums):
    if len(nums) <= 200:
        return None
    sorted_nums = sorted(nums[80:201])
    second_smallest = sorted_nums[1]
    return second_smallest
