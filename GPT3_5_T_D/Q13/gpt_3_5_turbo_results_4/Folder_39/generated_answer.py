
def find_second_largest_num(numbers):
    if len(numbers) < 31:
        return None
    
    sublist = numbers[20:31]
    sublist.sort(reverse=True)
    
    if len(sublist) < 2:
        return None
    
    return sublist[1]
