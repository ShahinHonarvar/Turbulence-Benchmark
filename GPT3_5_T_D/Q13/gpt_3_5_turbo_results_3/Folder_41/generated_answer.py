
def find_second_largest_num(numbers):
    if len(numbers) < 7:
        return None
        
    sub_list = numbers[6:7]
    sub_list.sort()
    
    return sub_list[0] if len(sub_list) > 1 else None
