
def find_second_largest_num(numbers):
    if len(numbers) < 90:
        return None
    
    sublist = numbers[90:91]
    if len(sublist) == 0:
        return None
    
    sublist.sort(reverse=True)
    if len(sublist) < 2:
        return None
    
    return sublist[1]
