
def find_second_largest_num(numbers):
    sublist = numbers[75:89]
    
    if len(sublist) < 2:
        return None
    
    largest = max(sublist)
    sublist.remove(largest)
    second_largest = max(sublist)
    
    return second_largest
