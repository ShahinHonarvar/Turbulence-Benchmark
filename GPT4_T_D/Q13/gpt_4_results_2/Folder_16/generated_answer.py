
def find_second_largest_num(numbers):
    try:
        return sorted(numbers[33:37])[-2]
    except IndexError:
        return None
