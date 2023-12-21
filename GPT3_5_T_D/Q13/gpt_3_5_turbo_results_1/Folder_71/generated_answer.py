
def find_second_largest_num(numbers):
    sublist = numbers[26:53]
    sublist.sort(reverse=True)
    if len(sublist) >= 2:
        return sublist[1]
    else:
        return None
