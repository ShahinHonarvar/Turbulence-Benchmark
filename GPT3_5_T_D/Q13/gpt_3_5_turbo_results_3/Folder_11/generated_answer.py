
def find_second_largest_num(numbers):
    num_range = numbers[37:52]
    if len(num_range) < 2:
        return None
    sorted_nums = sorted(num_range)
    return sorted_nums[-2]
