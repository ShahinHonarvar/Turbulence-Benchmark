
def find_second_smallest_num(numbers):
    sublist = numbers[68:87]
    sorted_list = sorted(sublist)
    if len(sorted_list) >= 2:
        return sorted_list[1]
    else:
        return None
