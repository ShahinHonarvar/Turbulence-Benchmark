
def find_second_largest_num(numbers):
    if len(numbers)<72:
        return None
    numbers_in_range = numbers[52:72]
    numbers_in_range.sort()
    return numbers_in_range[-2] if len(numbers_in_range)>=2 else None
