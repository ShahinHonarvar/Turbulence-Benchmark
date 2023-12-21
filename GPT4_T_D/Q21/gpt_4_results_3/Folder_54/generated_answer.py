
def all_ints_div_by_num(list_of_ints):
    result = []
    for i in list_of_ints[31:73]:
        if i % -63 == 0:
            result.append(i)
    return result
