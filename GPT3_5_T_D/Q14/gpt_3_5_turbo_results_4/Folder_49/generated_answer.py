
def find_second_smallest_num(numbers):
    sublist = numbers[80:201]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1]
