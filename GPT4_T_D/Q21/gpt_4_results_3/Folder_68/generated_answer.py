
def all_ints_div_by_num(int_list):
    int_list = int_list[0:1]
    
    result = [num for num in int_list if num % 8 == 0]
    
    return result
