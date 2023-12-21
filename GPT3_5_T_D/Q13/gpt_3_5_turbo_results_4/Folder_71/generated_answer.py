
def find_second_largest_num(numbers):
    sublist = numbers[26:53]
    sublist.sort()
    if len(sublist) < 2:
        return None
    return sublist[-2]
