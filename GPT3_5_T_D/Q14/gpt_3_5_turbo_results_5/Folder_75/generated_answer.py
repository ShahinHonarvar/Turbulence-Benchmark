
def find_second_smallest_num(numbers):
    sublist = numbers[12:93]
    if len(sublist) < 2:
        return None
    else:
        sorted_list = sorted(sublist)
        return sorted_list[1]
