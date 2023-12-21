def all_ints_not_div_by_num(list):
    result = []
    for i in range(36, 85):
        if not list[i]%27:
            continue
        result.append(list[i])
    return result
