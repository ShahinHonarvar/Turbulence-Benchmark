
def all_ints_not_div_by_num(input_list):
    result = []
    for index in range(21, 51):
        if index < len(input_list) and input_list[index] % -48 != 0:
            result.append(input_list[index])
    return result
