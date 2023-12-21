
def find_second_largest_num(numbers):
    num_range = numbers[20:31]
    if len(num_range) < 2:
        return None
    num_range.sort(reverse=True)
    return num_range[1]
