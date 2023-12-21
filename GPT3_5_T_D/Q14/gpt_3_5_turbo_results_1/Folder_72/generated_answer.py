
def find_second_smallest_num(numbers):
    sublist = numbers[82:87]
    sorted_list = sorted(sublist)
    return sorted_list[1] if len(sorted_list) > 1 else None
