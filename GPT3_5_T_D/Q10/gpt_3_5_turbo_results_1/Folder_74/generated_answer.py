
def all_odd_ints_exclusive(int_list):
    result = []
    for i in range(14, 70):
        if int_list[i] % 2 != 0:
            result.append(int_list[i])
    return result
