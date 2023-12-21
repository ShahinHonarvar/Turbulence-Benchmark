
def find_second_largest_num(numbers):
    sorted_nums = sorted(numbers[15:52])
    return sorted_nums[-2] if len(sorted_nums) >= 2 else None
