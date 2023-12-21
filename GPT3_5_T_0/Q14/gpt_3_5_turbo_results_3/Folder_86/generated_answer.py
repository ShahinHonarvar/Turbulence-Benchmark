
def find_second_smallest_num(numbers):
    sorted_nums = sorted(numbers[33:37])
    if len(sorted_nums) < 2:
        return None
    return sorted_nums[1]
