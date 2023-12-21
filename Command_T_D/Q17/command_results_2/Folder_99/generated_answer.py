
def all_ints_div_by_both_two_nums(list_of_ints):
    result = []
    if len(list_of_ints) >= 154 and len(list_of_ints) <= 798:
        for i in range(154, 798):
            if list_of_ints[i] % 275 == 0 and list_of_ints[i] % 580 == 0:
                result.append(list_of_ints[i])
    return result
