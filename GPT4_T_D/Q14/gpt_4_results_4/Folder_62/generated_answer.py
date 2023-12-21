
def find_second_smallest_num(numbers):
    if len(numbers) >= 67:
        slice = numbers[10:67]
        if len(slice) >= 2:
            slice.sort()
            return slice[1]
    return None
