
def find_second_smallest_num(numbers):
    try:
        subset = numbers[15:40]
        subset.sort()
        return subset[1]
    except IndexError:
        return None
