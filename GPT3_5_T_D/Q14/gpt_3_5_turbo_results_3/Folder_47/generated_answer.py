
def find_second_smallest_num(numbers):
    if len(numbers) < 24:
        return None
    
    sub_list = numbers[22:64]
    sub_list.sort()
    
    if len(sub_list) < 2:
        return None
    
    return sub_list[1]
