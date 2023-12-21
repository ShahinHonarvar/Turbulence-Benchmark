
def find_second_largest_num(numbers):
    if len(numbers) < 201:
        return None
    
    sublist = numbers[30:201]
    
    if len(sublist) < 2:
        return None
    
    largest = max(sublist)
    sublist.remove(largest)
    
    return max(sublist)
