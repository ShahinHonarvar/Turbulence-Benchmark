
def find_second_smallest_num(numbers):
    sublist = numbers[31:35]
    sublist.sort()
    return sublist[1] if len(sublist) > 1 else None
