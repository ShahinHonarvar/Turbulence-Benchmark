
def find_second_smallest_num(numbers):
    if len(numbers) < 51:
        return None
    sorted_nums = sorted(numbers[37:52])
    return sorted_nums[1] if len(sorted_nums) > 1 else None
