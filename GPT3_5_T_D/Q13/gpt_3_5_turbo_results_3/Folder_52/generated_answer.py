
def find_second_largest_num(numbers):
    selection = numbers[28:39]
    if len(selection) < 2:
        return None
    selection.sort()
    return selection[-2]
