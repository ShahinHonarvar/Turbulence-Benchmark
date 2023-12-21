
def find_second_smallest_num(numbers):
    sublist = numbers[60:201]
    if len(sublist) > 1:
        smallest = min(sublist)
        sublist.remove(smallest)
        return min(sublist)
    else:
        return None
