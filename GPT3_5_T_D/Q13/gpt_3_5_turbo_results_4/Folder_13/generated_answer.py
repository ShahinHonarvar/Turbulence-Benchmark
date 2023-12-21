
def find_second_largest_num(numbers):
    num_range = numbers[25:88]
    num_range.sort(reverse=True)
    if len(num_range) < 2:
        return None
    else:
        return num_range[1]
