
def find_second_smallest_num(numbers):
    sublist = numbers[56:83]
    if len(sublist) < 2:
        return None
    smallest = min(sublist)
    sublist.remove(smallest)
    return min(sublist) if sublist else None
