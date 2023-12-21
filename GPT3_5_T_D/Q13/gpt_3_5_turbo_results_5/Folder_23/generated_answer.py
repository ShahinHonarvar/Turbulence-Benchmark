
def find_second_largest_num(numbers):
    numbers_range = numbers[52:72]
    if len(numbers_range) > 1:
        numbers_range.sort()
        return numbers_range[-2]
    else:
        return None
