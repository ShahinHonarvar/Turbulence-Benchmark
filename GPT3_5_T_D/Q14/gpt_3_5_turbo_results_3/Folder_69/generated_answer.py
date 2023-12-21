
def find_second_smallest_num(numbers):
    sorted_nums = sorted(numbers[25:88])
    return sorted_nums[1] if len(sorted_nums) > 1 else None
