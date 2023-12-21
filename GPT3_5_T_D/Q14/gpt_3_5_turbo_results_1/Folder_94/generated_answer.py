
def find_second_smallest_num(numbers):
    sublist = numbers[52:72]
    if len(sublist) < 2:
        return None
    
    smallest = min(sublist)
    sublist.remove(smallest)
    second_smallest = min(sublist)
    return second_smallest
