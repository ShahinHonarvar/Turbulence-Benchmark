
def find_second_smallest_num(numbers):
    sublist = numbers[37:52]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1]
