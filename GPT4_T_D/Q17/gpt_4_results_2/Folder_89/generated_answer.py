
def all_ints_div_by_both_two_nums(input_list):
    result = []
    for i in range(28, 97):
        if input_list[i] % 90 == 0 and input_list[i] % 97 == 0:
            result.append(input_list[i])
    return result
