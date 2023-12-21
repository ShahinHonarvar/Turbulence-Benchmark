
def find_second_smallest_num(nums):
    if len(nums) < 55:
        return None
    sorted_nums = sorted(nums)[49:55]
    second_smallest = sorted_nums[1]
    return second_smallest
