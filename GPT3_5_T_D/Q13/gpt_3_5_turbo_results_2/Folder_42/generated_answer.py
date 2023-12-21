
def find_second_largest_num(numbers):
    second_largest = None
    sublist = numbers[29:80]
    if len(sublist) >= 2:
        largest = max(sublist)
        sublist.remove(largest)
        second_largest = max(sublist)
    return second_largest
