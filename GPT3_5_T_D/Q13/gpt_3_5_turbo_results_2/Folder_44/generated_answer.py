
def find_second_largest_num(numbers):
    sublist = numbers[13:69]
    if len(sublist) < 2:
        return None
    elif len(sublist) == 2:
        return min(sublist)
    else:
        sublist.sort()
        return sublist[-2]
