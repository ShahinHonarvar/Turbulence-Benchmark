
def all_ints_not_div_by_num(num_list):
    result = []
    for num in num_list[16:20]:
        if num % 93 != 0:
            result.append(num)
    return result
