
def find_second_largest_num(numbers):
    sublist = numbers[62:100]
    if len(sublist) < 2:
        return None
    sublist.sort(reverse=True)
    return sublist[1]
