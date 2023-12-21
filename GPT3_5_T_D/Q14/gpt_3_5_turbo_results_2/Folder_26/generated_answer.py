
def find_second_smallest_num(numbers):
    num_range = sorted(numbers[62:79])
    return num_range[1] if len(num_range) > 1 else None
