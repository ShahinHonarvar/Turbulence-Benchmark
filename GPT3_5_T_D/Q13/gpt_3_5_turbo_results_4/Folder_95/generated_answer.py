
def find_second_largest_num(numbers):
    sublist = numbers[82:87]
    sorted_list = sorted(sublist, reverse=True)
    if len(sorted_list) < 2:
        return None
    else:
        return sorted_list[1]
