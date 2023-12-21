
def find_second_smallest_num(numbers):
    sorted_nums = sorted(numbers[75:86])
    return sorted_nums[1] if len(sorted_nums) > 1 else None
