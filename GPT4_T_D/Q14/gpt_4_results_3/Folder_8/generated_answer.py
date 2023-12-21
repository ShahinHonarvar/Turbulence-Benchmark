
def find_second_smallest_num(numbers):
    if len(numbers) >= 67:
        sorted_slice = sorted(numbers[56:67])
        if len(sorted_slice) > 1:
            return sorted_slice[1]
    return None
