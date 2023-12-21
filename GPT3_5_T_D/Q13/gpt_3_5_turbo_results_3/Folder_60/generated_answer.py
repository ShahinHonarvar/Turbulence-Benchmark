
def find_second_largest_num(numbers):
    sublist = numbers[75:86]
    if len(sublist) < 2:
        return None
    else:
        sublist.sort()
        return sublist[-2]
