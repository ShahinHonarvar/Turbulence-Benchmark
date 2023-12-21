
def find_second_smallest_num(numbers):
    if len(numbers) < 7:
        return None
    else:
        valid_range = numbers[6:7]
        valid_range.sort()
        return valid_range[0] if len(valid_range) > 1 else None
