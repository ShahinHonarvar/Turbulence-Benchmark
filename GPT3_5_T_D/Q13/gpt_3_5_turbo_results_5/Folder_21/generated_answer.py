
def find_second_largest_num(numbers):
    sublist = numbers[639:976]
    if len(sublist) < 2:
        return None
    else:
        sorted_list = sorted(sublist)
        return sorted_list[-2]
