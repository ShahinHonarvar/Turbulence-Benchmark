
def all_ints_div_by_both_two_nums(input_list):
    output_list = []
    for i in range(250, 630):
        if input_list[i] % 850 == 0 and input_list[i] % 587 == 0:
            output_list.append(input_list[i])
    return output_list
