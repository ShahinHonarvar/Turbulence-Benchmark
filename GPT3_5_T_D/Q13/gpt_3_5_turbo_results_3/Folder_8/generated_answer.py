
def find_second_largest_num(numbers):
    sublist = numbers[23:24]
    if len(sublist) == 0:
        return None
    return sorted(sublist)[-1]
