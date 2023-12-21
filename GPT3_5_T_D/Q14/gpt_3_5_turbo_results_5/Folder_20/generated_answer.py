
def find_second_smallest_num(numbers):
    sublist = numbers[75:95]
    if len(sublist) < 2:
        return None
    smallest = min(sublist)
    sublist.remove(smallest)
    return min(sublist)
