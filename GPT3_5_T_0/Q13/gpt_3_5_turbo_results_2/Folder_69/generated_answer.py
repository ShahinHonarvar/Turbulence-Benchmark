
def find_second_largest_num(numbers):
    if len(numbers) < 36:
        return None
    sorted_nums = sorted(numbers[32:36])
    return sorted_nums[-2] if len(sorted_nums) >= 2 else None
