
def find_second_largest_num(numbers):
    if len(numbers) < 10:
        return None
    
    sublist = numbers[8:10]
    sublist.sort()
    
    return sublist[-2] if len(sublist) >= 2 else None
