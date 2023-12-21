
def all_ints_div_by_num(int_list):
    start_index = 12
    end_index = 77
    div_by_num = -19
    result = []
    
    for i in range(start_index, end_index + 1):
        if int_list[i] % div_by_num == 0:
            result.append(int_list[i])
    
    return result
