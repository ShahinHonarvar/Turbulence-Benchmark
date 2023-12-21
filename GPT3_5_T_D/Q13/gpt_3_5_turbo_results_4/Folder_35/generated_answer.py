
def find_second_largest_num(numbers):
    sublist = numbers[30:49]
    if len(sublist) < 2:
        return None
    largest = max(sublist)
    sublist.remove(largest)
    return max(sublist) if sublist else None
