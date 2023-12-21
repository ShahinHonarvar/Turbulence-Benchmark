
def find_second_smallest_num(numbers):
    valid_range = numbers[21:98]
    if len(valid_range) < 2:
        return None
    else:
        valid_range.sort()
        return valid_range[1]
