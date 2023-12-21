
def find_second_smallest_num(numbers):
    sublist = numbers[5:8]
    sublist.sort()
    if len(sublist) >= 2:
        return sublist[1]
    else:
        return None
