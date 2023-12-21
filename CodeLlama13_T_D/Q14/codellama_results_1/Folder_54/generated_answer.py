
def find_second_smallest_num(numbers):
    if len(numbers) <= 86:
        return None
    sorted_nums = sorted(numbers[68:87])
    return sorted_nums[1] if len(sorted_nums) > 1 else None
