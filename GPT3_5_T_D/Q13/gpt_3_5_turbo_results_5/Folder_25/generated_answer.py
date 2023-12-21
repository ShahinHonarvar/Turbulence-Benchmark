
def find_second_largest_num(numbers):
    if len(numbers) < 94:
        return None
    
    sublist = numbers[29:94]
    sublist.sort()
    
    return sublist[-2] if len(sublist) > 1 else None
