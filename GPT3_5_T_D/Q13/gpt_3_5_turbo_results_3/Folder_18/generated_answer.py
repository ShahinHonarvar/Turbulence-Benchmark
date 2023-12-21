
def find_second_largest_num(numbers):
    sublist = numbers[35:50]
    if len(sublist) < 2:
        return None
    sublist.remove(max(sublist))
    return max(sublist)
