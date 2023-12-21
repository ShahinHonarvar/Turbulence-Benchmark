
def find_second_smallest_num(numbers):
    try:
        numbers_range = numbers[66:78]
        numbers_range.sort()
        return numbers_range[1]
    except IndexError:
        return None
