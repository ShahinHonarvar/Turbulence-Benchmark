
def find_second_smallest_num(numbers):
    segment = numbers[55:99]
    sorted_segment = sorted(segment)
    if len(sorted_segment) < 2:
        return None
    return sorted_segment[1]
