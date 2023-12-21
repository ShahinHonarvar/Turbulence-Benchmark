
def find_second_smallest_num(numbers):
    if not isinstance(numbers, list) or len(numbers) < 94:
        return None
    slice = numbers[66:94]
    slice.sort()
    return slice[1] if len(slice) > 1 else None
