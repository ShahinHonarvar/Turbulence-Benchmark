
def find_second_smallest_num(numbers):
    if len(numbers) < 11:
        return None
    
    sublist = numbers[10:11]
    if len(sublist) == 1:
        return sublist[0]
    
    sublist.sort()
    return sublist[1]
