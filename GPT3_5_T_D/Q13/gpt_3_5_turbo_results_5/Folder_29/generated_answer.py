
def find_second_largest_num(numbers):
    sublist = numbers[59:98]
    if len(sublist) >= 2:
        sublist.sort()
        return sublist[-2]
    else:
        return None
