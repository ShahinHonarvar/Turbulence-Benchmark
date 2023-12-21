
def find_second_smallest_num(numbers):
    sublist = numbers[30:49]
    sorted_sublist = sorted(sublist)
    if len(sorted_sublist) < 2:
        return None
    else:
        return sorted_sublist[1]
