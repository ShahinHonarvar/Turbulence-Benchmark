
def find_second_smallest_num(numbers):
    sorted_nums = sorted(numbers[40:201])
    return sorted_nums[1] if len(sorted_nums) >= 2 else None
