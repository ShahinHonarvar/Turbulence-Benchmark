
def all_ints_div_by_both_two_nums(num_list):
    output_list = []
    for i in range(46, 92):
        if num_list[i] % 67 == 0 and num_list[i] % 15 == 0:
            output_list.append(num_list[i])
    return output_list
