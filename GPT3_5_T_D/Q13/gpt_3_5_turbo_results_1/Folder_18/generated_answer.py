
def find_second_largest_num(numbers):
    sublist = numbers[35:50]
    if len(sublist) < 2:
        return None
    largest = max(sublist)
    sublist.remove(largest)
    return max(sublist)
