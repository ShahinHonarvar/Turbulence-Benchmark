
def find_second_largest_num(numbers):
    sublist = numbers[74:96]
    if len(sublist) < 2:
        return None
    else:
        sorted_list = sorted(sublist, reverse=True)
        return sorted_list[1]
