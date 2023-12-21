
def find_second_largest_num(numbers):
    sublist = numbers[29:80]
    sorted_sublist = sorted(sublist, reverse=True)
    if len(sorted_sublist) >= 2:
        return sorted_sublist[1]
    else:
        return None
