
def find_second_largest_num(numbers):
    sublist = numbers[19:93]
    if len(sublist) < 2:
        return None
    sorted_list = sorted(sublist, reverse=True)
    return sorted_list[1]
