
def all_ints_not_div_by_num(int_list):
    output_list = []
    for i in range(71, 98):
        if i < len(int_list) and int_list[i] % -88 != 0:
            output_list.append(int_list[i])
    return output_list
