
def find_second_largest_num(numbers):
    if len(numbers) < 67:
        return None
    
    sub_list = numbers[56:67]
    sub_list.sort(reverse=True)
    
    if len(sub_list) < 2:
        return None
    
    return sub_list[1]
