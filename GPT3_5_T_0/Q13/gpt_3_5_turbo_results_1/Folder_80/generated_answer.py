
def find_second_largest_num(numbers):
    if len(numbers) < 67:
        return None
    sorted_nums = sorted(numbers[64:67])
    return sorted_nums[-2] if len(sorted_nums) >= 2 else None
