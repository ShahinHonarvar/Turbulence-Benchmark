
def find_second_smallest_num(numbers):
    sublist = numbers[209:557]
    sublist.sort()
    if len(sublist) < 2:
        return None
    else:
        return sublist[1]
