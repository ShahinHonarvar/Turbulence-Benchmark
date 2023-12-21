
def find_second_smallest_num(numbers):
    segment = numbers[6:9]
    if len(segment) < 2:
        return None
    segment.sort()
    return segment[1]
