
def find_second_smallest_num(numbers):
    sublist = numbers[37:77]
    sublist.sort()
    if len(sublist) > 1:
        return sublist[1]
    else:
        return None
