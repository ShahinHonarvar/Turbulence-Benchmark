
def find_second_largest_num(numbers):
    sublist = numbers[75:86]
    sublist.sort(reverse=True)
    return sublist[1] if len(sublist) > 1 else None
