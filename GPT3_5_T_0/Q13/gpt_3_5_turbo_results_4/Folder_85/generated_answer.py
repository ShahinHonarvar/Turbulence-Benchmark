
def find_second_largest_num(numbers):
    sublist = numbers[6:9]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]
