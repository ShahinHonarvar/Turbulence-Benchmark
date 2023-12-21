
def find_second_largest_num(numbers):
    sublist = numbers[3:6]
    sorted_sublist = sorted(sublist)
    if len(sorted_sublist) >= 2:
        return sorted_sublist[-2]
    else:
        return None
