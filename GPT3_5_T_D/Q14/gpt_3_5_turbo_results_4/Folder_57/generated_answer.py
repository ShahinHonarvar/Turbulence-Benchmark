
def find_second_smallest_num(numbers):
    sublist = numbers[20:31]
    sublist.sort()
    if len(sublist) < 2:
        return None
    return sublist[1]
