
def find_second_largest_num(numbers):
    sublist = numbers[37:77]
    sorted_sublist = sorted(sublist, reverse=True)
    if len(sorted_sublist) < 2:
        return None
    else:
        return sorted_sublist[1]
