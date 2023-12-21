
def all_ints_div_by_both_two_nums(num_list: list) -> list:
    result = []
    for i in num_list[1:9]:
        if i % -9 == 0 and i % -3 == 0:
            result.append(i)
    return result
