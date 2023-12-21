
def all_odd_ints_inclusive(my_list):
    result = []
    for i in range(6, 9):
        if my_list[i] % 2 != 0:
            result.append(my_list[i])
    return result
