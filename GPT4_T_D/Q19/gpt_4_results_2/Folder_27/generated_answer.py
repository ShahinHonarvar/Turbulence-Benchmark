
def all_ints_not_div_by_num(int_list):
    result = []
    for i in range(15, 21):
        try:
            if int_list[i] % -93 != 0:
                result.append(int_list[i])
        except IndexError:
            break
    return result
