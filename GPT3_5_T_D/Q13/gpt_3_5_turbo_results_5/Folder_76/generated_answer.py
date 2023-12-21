
def find_second_largest_num(numbers):
    sublist = numbers[686:988]
    if len(sublist) < 2:
        return None
    max_num = max(sublist)
    sublist.remove(max_num)
    return max(sublist)
