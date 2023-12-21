
def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    sorted_nums = sorted(numbers)
    return sorted_nums[1] if len(sorted_nums) > 1 else None
