
def find_second_smallest_num(numbers):
    slice = numbers[29:52]
    sorted_slice = sorted(slice)
    if len(sorted_slice) >= 2:
        return sorted_slice[1]
    else:
        return None
