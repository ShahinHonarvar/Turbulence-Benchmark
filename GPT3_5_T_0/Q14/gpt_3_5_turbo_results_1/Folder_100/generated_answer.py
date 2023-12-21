
def find_second_smallest_num(numbers):
    sublist = numbers[43:52]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1]
