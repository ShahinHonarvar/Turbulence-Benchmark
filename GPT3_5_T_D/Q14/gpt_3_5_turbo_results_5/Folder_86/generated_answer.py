
def find_second_smallest_num(numbers):
    sublist = numbers[33:37]
    if len(sublist) < 2:
        return None
    sublist = sorted(sublist)
    return sublist[1]
