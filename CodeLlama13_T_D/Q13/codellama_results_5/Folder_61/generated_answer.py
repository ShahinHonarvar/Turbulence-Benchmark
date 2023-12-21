
def find_second_largest_num(my_list):
    if len(my_list) < 8:
        return None
    
    sorted_list = sorted(my_list)[7:]
    second_largest = None
    for i in range(len(sorted_list)):
        if sorted_list[i] == sorted_list[-1]:
            continue
        else:
            second_largest = sorted_list[i]
            break
    
    return second_largest
