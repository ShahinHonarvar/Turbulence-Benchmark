
def all_ints_div_by_both_two_nums(num_list):
    result = []
    for index in range(69, 98):
        if num_list[index] % -90 == 0 and num_list[index] % -67 == 0:
            result.append(num_list[index])
    return result
