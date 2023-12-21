
def find_second_smallest_num(numbers):
    subset = numbers[68:87]
    if len(subset) < 2:
        return None
    else:
        return sorted(subset)[1]
