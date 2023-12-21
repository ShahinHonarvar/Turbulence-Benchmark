
def all_ints_div_by_num(my_list):
    start = 70
    end = 76
    result = []
    for i in range(start, end+1):
        if my_list[i] % -92 == 0:
            result.append(my_list[i])
    return result
