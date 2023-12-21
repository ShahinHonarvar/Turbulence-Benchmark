 
def find_second_smallest_num(numbers):
    sublist = numbers[23:24]
    sorted_sublist = sorted(sublist)
    if len(sorted_sublist) < 2:
        return None
    return sorted_sublist[1]
