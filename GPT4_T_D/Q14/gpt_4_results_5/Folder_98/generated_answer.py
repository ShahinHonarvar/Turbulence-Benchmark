
def find_second_smallest_num(numbers):
    slice = numbers[6:7]
    if not slice:
        return None
    else:
        return sorted(slice)[1] if len(slice) > 1 else None
