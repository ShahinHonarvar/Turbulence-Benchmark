
def find_second_largest_num(numbers):
    sublist = numbers[43:52]
    if len(sublist) > 1:
        sublist.sort()
        return sublist[-2]
    else:
        return None
