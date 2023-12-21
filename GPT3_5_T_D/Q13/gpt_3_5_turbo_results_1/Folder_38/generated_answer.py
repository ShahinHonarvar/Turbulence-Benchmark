
def find_second_largest_num(numbers):
    if len(numbers) < 64:
        return None
    
    sublist = numbers[22:64]
    sublist.sort()
    
    if len(sublist) < 2:
        return None
    
    return sublist[-2]
