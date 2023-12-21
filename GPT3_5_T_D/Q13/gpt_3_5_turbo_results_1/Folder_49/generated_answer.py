
def find_second_largest_num(numbers):
    sublist = numbers[80:201]
    if len(sublist) < 2:
        return None
    
    max_num = max(sublist)
    sublist.remove(max_num)
    second_largest = max(sublist)
    return second_largest
