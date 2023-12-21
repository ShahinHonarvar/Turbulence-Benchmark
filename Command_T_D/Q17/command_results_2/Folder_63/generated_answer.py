
def all_ints_div_by_both_two_nums(list_of_ints):
    result = []
    for index in range(31, 51):
        if list_of_ints[index] % 81 == 0 and list_of_ints[index] % 64 == 0:
            result.append(list_of_ints[index])
    return result
