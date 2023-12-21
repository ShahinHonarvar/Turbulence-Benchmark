
def find_second_smallest_num(numbers):
    if len(numbers) < 37:
        return None
    sorted_nums = sorted(numbers[33:37])
    return sorted_nums[1] if len(sorted_nums) > 1 else None
