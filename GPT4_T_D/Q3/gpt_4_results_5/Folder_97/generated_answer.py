
def all_pos_ints_inclusive(integer_list):
    result = []
    sub_list = integer_list[40:81]
    for num in sub_list:
        if num > 0:
            result.append(num)
    return result
