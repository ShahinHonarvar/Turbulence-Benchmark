
def find_second_largest_num(numbers):
    sublist = numbers[32:36]
    if len(set(sublist)) < 2:
        return None
    sublist.remove(max(sublist))
    return max(sublist)
