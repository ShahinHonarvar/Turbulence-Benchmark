
def find_second_smallest_num(numbers):
    if not numbers or len(numbers) < 93:
        return None
    sorted_nums = sorted(numbers[29:94])
    return sorted_nums[1] if len(sorted_nums) > 1 else None
