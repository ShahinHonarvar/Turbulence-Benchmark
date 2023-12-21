
def find_second_smallest_num(numbers):
    sublist = numbers[17:79]
    if len(sublist) < 2:
        return None
    else:
        sorted_list = sorted(sublist)
        return sorted_list[1]
