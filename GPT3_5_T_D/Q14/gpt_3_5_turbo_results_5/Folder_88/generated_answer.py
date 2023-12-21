
def find_second_smallest_num(numbers):
    sub_list = numbers[6:9]
    sub_list.sort()
    
    if len(sub_list) < 2:
        return None
    else:
        return sub_list[1]
