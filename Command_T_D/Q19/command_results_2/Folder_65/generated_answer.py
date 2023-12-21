def all_ints_not_div_by_num(num_list):
    result = []
    for item in num_list[15:51]:
        if not item % -34:
            continue
        result.append(item)
    return result
