
def find_second_largest_num(numbers):
    sublist = numbers[25:60]
    sublist.sort(reverse=True)
    if len(sublist) > 1:
        return sublist[1]
    else:
        return None
