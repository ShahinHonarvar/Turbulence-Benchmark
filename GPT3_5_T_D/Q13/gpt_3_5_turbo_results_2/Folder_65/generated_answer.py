
def find_second_largest_num(numbers):
    if len(numbers) < 99:
        return None
    
    sublist = numbers[56:99]
    sublist.sort()
    
    if len(sublist) < 2:
        return None
    else:
        return sublist[-2]
