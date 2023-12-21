
def all_ints_div_by_both_two_nums(list):
    result = []
    for index in range(51, 77):
        if list[index] % -90 == 0 and list[index] % -59 == 0:
            result.append(list[index])
    return result
