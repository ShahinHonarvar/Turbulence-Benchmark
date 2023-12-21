
def find_second_smallest_num(numbers):
    sublist = numbers[19:93]
    sorted_list = sorted(sublist)
    if len(sorted_list) < 2:
        return None
    return sorted_list[1]
