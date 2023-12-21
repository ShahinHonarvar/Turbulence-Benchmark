
def find_second_largest_num(numbers):
    if len(numbers) < 96:
        return None
    
    sub_list = numbers[74:96]
    sub_list.sort()
    return sub_list[-2] if len(sub_list) >= 2 else None
