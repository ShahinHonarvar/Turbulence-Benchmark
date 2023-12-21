
def find_second_largest_num(numbers):
    index_range = numbers[75:89]
    if not index_range:
        return None
    else:
        index_range.sort()
        return index_range[-2]
