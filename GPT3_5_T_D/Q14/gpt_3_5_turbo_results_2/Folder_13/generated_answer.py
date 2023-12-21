
def find_second_smallest_num(numbers):
    sublist = numbers[28:33]
    if len(sublist) < 2:
        return None
    sorted_sublist = sorted(sublist)
    return sorted_sublist[1]
