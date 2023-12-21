
def all_ints_div_by_both_two_nums(num_list):
    output_list = []
    for i in range(90, 97 + 1):
        if num_list[i] % 13 == 0 and num_list[i] % 35 == 0:
            output_list.append(num_list[i])
    return output_list
