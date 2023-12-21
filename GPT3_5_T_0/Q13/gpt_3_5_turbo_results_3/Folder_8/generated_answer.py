
def find_second_largest_num(numbers):
    if len(numbers) < 24:
        return None
    sorted_nums = sorted(numbers[23:24+1])
    return sorted_nums[-2] if len(sorted_nums) >= 2 else None
