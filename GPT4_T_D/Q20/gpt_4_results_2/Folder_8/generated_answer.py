
def find_n_th_smallest_num(numbers):
    if len(numbers) < 32:
        raise ValueError("Input list is not long enough")
    
    sublist = numbers[15:32]
    sublist.sort()
    
    return sublist[9]
