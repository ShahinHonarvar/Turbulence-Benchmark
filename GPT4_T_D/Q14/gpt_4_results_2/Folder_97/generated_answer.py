
def find_second_smallest_num(numbers):
    if len(numbers) < 35:
        return 'None'
    
    sublist = numbers[31:35]
    sublist.sort()
    if len(sublist) < 2:
        return 'None'
    else:
        return sublist[1]
