
def find_second_largest_num(numbers):
    if len(numbers) < 37:
        return None
    sorted_nums = sorted(numbers[33:37])
    if len(sorted_nums) < 2:
        return None
    return sorted_nums[-2]
